# mkdocs-wiki

[Notifiarr wiki](https://notifiarr.wiki) source.

## Local Build

### macOS

```bash
brew install python3
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
mkdocs serve
```

### Windows

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
mkdocs serve
```

### Linux

```bash
sudo apt install python3 || sudo yum install python3
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
mkdocs serve
```

Once `mkdocs serve` is running, open <http://127.0.0.1:8000> to preview the site with live reload.

## Contributing

Documentation lives under `docs/`. Pages are Markdown; the navigation is defined in `mkdocs.yml`.

This repo uses [pre-commit](https://pre-commit.com) to lint docs (markdownlint, cspell, line endings). Install the hooks once:

```bash
pip install pre-commit
pre-commit install
```

Every commit is then checked automatically. To run everything manually:

```bash
pre-commit run --all-files
mkdocs build --strict   # catches broken internal links and anchors
```

- **Spelling** — cspell is configured in `.cspell.json`. If it flags a real product name or CLI term, add it to the `words` array. Fix genuine typos in the prose rather than adding them to the dictionary.
- **Markdown style** — rules are in `.markdownlint.yaml`.
- **Line endings** — files are normalized to LF via `.gitattributes`; keep your editor set to LF.

Open a pull request against `main`. CI builds the site with `--strict` and runs pre-commit; GitHub Pages deploys on merge.
