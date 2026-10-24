"""Build the wiki once and check that the rendered site is complete."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}


class ConfigLoader(yaml.SafeLoader):
    """Load mkdocs.yml, including the python/name emoji tags."""


def _python_name(loader: yaml.SafeLoader, suffix: str, node: yaml.Node) -> str:
    return suffix


ConfigLoader.add_multi_constructor("tag:yaml.org,2002:python/name:", _python_name)


class RefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for key in ("href", "src"):
            value = values.get(key)
            if value:
                self.refs.append((key, value))
        srcset = values.get("srcset")
        if not srcset:
            return
        for part in srcset.split(","):
            url = part.strip().split()[0] if part.strip() else ""
            if url:
                self.refs.append(("srcset", url))


def load_config() -> dict:
    return yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=ConfigLoader)


def nav_paths(node: object) -> list[str]:
    if isinstance(node, list):
        paths: list[str] = []
        for item in node:
            paths.extend(nav_paths(item))
        return paths
    if isinstance(node, dict):
        paths = []
        for value in node.values():
            if isinstance(value, str):
                paths.append(value)
            else:
                paths.extend(nav_paths(value))
        return paths
    return []


def html_for(md_rel: str, directory_urls: bool) -> Path:
    path = Path(md_rel)
    if not directory_urls:
        return path.with_suffix(".html")
    if path.name == "index.md":
        parent = path.parent
        return Path("index.html") if parent == Path(".") else parent / "index.html"
    return path.with_suffix("") / "index.html"


def canonical_path(path: str) -> str:
    path = unquote(path.split("#", 1)[0].split("?", 1)[0]).strip("/")
    if path in {"", "index.html"}:
        return ""
    suffix = "/index.html"
    if path.endswith(suffix):
        path = path[: -len(suffix)]
    return path


def page_keys(paths: list[str], directory_urls: bool) -> set[str]:
    return {canonical_path(html_for(path, directory_urls).as_posix()) for path in paths}


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config()


@pytest.fixture(scope="session")
def site_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    override = os.environ.get("MKDOCS_SITE_DIR")
    if override:
        dest = Path(override)
        if not dest.is_absolute():
            dest = ROOT / dest
        dest.mkdir(parents=True, exist_ok=True)
    else:
        dest = tmp_path_factory.mktemp("site")

    result = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--site-dir", str(dest)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError("mkdocs build --strict failed\n" + result.stdout + "\n" + result.stderr)
    return dest


def test_every_markdown_file_is_in_the_nav(config: dict) -> None:
    documented = {path.relative_to(DOCS).as_posix() for path in DOCS.rglob("*.md")}
    listed = set(nav_paths(config["nav"]))
    orphans = sorted(documented - listed)
    missing = sorted(listed - documented)
    assert not orphans, "markdown files missing from nav:\n" + "\n".join(orphans)
    assert not missing, "nav entries without a markdown file:\n" + "\n".join(missing)


def test_nav_pages_render(config: dict, site_dir: Path) -> None:
    directory_urls = config.get("use_directory_urls", True)
    missing = []
    for md_rel in nav_paths(config["nav"]):
        html_path = site_dir / html_for(md_rel, directory_urls)
        if not html_path.is_file():
            missing.append(f"{md_rel} -> {html_path}")
            continue
        text = html_path.read_text(encoding="utf-8")
        if "headerlink" not in text:
            missing.append(f"{html_path} has no permalink")
    assert not missing, "\n".join(missing)


def test_home_page_contains_site_name_and_heading(config: dict, site_dir: Path) -> None:
    html = (site_dir / "index.html").read_text(encoding="utf-8")
    assert config["site_name"] in html
    heading = re.search(r"<h1\b[^>]*>(.*?)</h1>", html, re.DOTALL)
    assert heading is not None
    assert "Notifiarr" in heading.group(1)


def test_search_index_includes_every_page(config: dict, site_dir: Path) -> None:
    payload = json.loads((site_dir / "search" / "search_index.json").read_text(encoding="utf-8"))
    found = set()
    for doc in payload["docs"]:
        location = doc.get("location", doc.get("url", ""))
        found.add(canonical_path(str(location)))
    expected = page_keys(nav_paths(config["nav"]), config.get("use_directory_urls", True))
    missing = sorted(expected - found)
    assert not missing, "pages missing from search index:\n" + "\n".join(missing)


def test_sitemap_lists_every_page(config: dict, site_dir: Path) -> None:
    root = ElementTree.parse(site_dir / "sitemap.xml").getroot()
    locs = [node.text or "" for node in root.iter() if node.tag.endswith("loc") and node.text]
    site_url = str(config["site_url"]).rstrip("/")
    found = set()
    for loc in locs:
        if loc.startswith(site_url):
            loc = loc[len(site_url) :]
        found.add(canonical_path(loc))
    expected = page_keys(nav_paths(config["nav"]), config.get("use_directory_urls", True))
    missing = sorted(expected - found)
    assert not missing, "pages missing from sitemap:\n" + "\n".join(missing)


def test_extra_css_is_linked(site_dir: Path) -> None:
    css = site_dir / "stylesheets" / "github-permalink-style.css"
    assert css.is_file()
    assert css.stat().st_size > 0
    html = (site_dir / "index.html").read_text(encoding="utf-8")
    assert "stylesheets/github-permalink-style.css" in html


def test_logo_and_favicon_exist(site_dir: Path) -> None:
    assert (site_dir / "assets" / "logo.png").is_file()
    assert (site_dir / "assets" / "favicon.ico").is_file()


def test_glightbox_assets_exist(site_dir: Path) -> None:
    assets = [path for path in site_dir.rglob("*") if "glightbox" in path.name.lower()]
    assert assets, "GLightbox assets were not copied into the built site"


def local_target(page: Path, site: Path, url: str) -> Path | None:
    parsed = urlparse(url.strip())
    if parsed.scheme in SKIP_SCHEMES or parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if path == "":
        return None
    if path.startswith("/"):
        target = (site / path.lstrip("/")).resolve()
    else:
        target = (page.parent / path).resolve()
    if not target.is_file() and (target / "index.html").is_file():
        target = target / "index.html"
    return target


def test_local_refs_resolve(site_dir: Path) -> None:
    site = site_dir.resolve()
    problems: list[str] = []
    for page in site.rglob("*.html"):
        parser = RefParser()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))
        for kind, url in parser.refs:
            target = local_target(page, site, url)
            if target is None:
                continue
            try:
                target.relative_to(site)
            except ValueError:
                problems.append(f"{page.relative_to(site)} {kind}={url} escapes the site")
                continue
            if not target.is_file():
                problems.append(f"{page.relative_to(site)} {kind}={url}")
    assert not problems, f"{len(problems)} broken local refs:\n" + "\n".join(problems[:40])
