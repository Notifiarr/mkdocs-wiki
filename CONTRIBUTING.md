# Contributing to Notifiarr Wiki

Thanks for helping improve the Notifiarr Wiki. This guide covers how to report issues, set up your local environment, and submit changes.

## Ways to contribute

- Fix typos, broken links, or unclear wording in existing pages.
- Add documentation for new Notifiarr features or integrations.
- Improve diagrams, examples, or screenshots.
- Report content gaps or technical errors via the issue tracker.

If you're new to open source, look for issues labeled `good first issue`.

## Reporting issues

Open an issue on this repository describing:

- What page or section the problem affects (link or path).
- What you expected the docs to say.
- What the docs actually say (or where they're missing).
- Optionally: a suggested fix.

For Notifiarr application bugs (not docs bugs), please file in the [Notifiarr application repository](https://github.com/Notifiarr/notifiarr/issues) instead.

## Local development

The wiki is built with [MkDocs](https://www.mkdocs.org/) + Material theme. You need Python 3.12+.

```bash
git clone https://github.com/Notifiarr/mkdocs-wiki.git
cd mkdocs-wiki
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. Edits to `docs/` reload automatically.

Before opening a PR, run:

```bash
mkdocs build --strict
```

The `--strict` flag fails on any warning (broken internal links, missing nav entries, etc.) and matches what CI runs.

## Submitting changes

1. Fork the repository and create a feature branch from `main`:

    ```bash
    git checkout -b docs/short-description
    ```

2. Make your edits. Keep each PR focused on one logical change.

3. Commit with a descriptive message. Conventional Commits format is appreciated but not required:

    ```text
    docs(integrations): clarify Plex token scoping
    chore(ci): bump setup-python to v6
    fix(nav): remove dead link from getting-started
    ```

4. Push your branch to your fork and open a pull request against `Notifiarr/mkdocs-wiki:main`.

5. CI will run `mkdocs build --strict` against your PR. Address any warnings before requesting review.

## Style notes

- Use sentence case for headings (`## Getting started`, not `## Getting Started`) unless referring to a proper noun.
- Use fenced code blocks with a language tag for syntax highlighting (`` ```bash ``, `` ```yaml ``).
- Prefer relative links between docs pages (`[setup](../setup.md)`) so the strict build catches breakage.
- Screenshots go in `docs/images/` with descriptive filenames.

## Communication

- General questions about Notifiarr: the [Notifiarr Discord](https://notifiarr.com/discord).
- Wiki-specific questions: comment on the relevant issue or PR.

## License

By contributing, you agree your contributions are licensed under the same license as this repository.
