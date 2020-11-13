SHELL := /bin/bash

merge:
		@echo "Merging files into a single markdown file..."
		cat essays/*.md > graham.md

words:
		@echo "Counting words..."
		wc --words essays/* | sort -n

venv:
		python3 -m venv .venv
		source .venv/bin/activate
		pip install -r requirements.txt

epub:
		${merge_files}
		@echo "Pandoc is doing the EPUB heavy-lifting..."
		pandoc graham.md -o graham.epub -f gfm --metadata title="Paul Graham Essays"
		@echo "EPUB file created ✅"
