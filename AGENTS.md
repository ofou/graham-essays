## Cursor Cloud specific instructions

This is a Python CLI tool (single script `graham.py`) that scrapes Paul Graham's essays and builds an EPUB ebook. There is no web server, no database, and no test suite.

### System dependencies

- **Python 3** (pre-installed)
- **uv** (`~/.local/bin/uv`) — Python package manager; installed via `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **pandoc** (`apt install pandoc`) — converts Markdown to EPUB
- **GNU Make** (pre-installed)

Ensure `$HOME/.local/bin` is on `PATH` for `uv` to work.

### Running the pipeline

See `Makefile` for all targets. The full build is:

```
make venv    # create .venv and install Python deps
make fetch   # download 230+ essays (~25s with network)
make merge   # combine into graham.md
make epub    # build graham.epub (requires cover.png in repo root)
```

Or simply `make all` (which also runs `dependencies` and `wordcount`).

### Gotchas

- `make fetch` requires internet access to paulgraham.com. It takes ~25 seconds and writes 230 markdown files to `essays/`.
- `make epub` produces pandoc warnings about duplicate footnote references; this is expected and does not affect the output.
- The `cover.png` file must exist for the EPUB cover image. It is tracked in the repo.
- `make pdf` requires `calibre` (`ebook-convert`), which is optional and not needed for the standard pipeline.
- There are no automated tests. Correctness is verified by running the pipeline end-to-end and checking that `graham.epub`, `graham.md`, and `essays.csv` are generated.
- The `dependencies` Makefile target uses `sudo apt` on Linux, which may prompt for a password; install pandoc and uv manually if needed.
