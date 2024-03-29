SHELL := /bin/bash

.SILENT: clean venv fetch merge epub pdf

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
PKG_MANAGER := brew
VENV_ACTIVATE := source .venv/bin/activate
else ifeq ($(UNAME_S),Linux)
PKG_MANAGER := apt
VENV_ACTIVATE := . ./.venv/bin/activate
else
$(error Unsupported operating system: $(UNAME_S))
endif

all: dependencies clean venv fetch merge epub wordcount

clean:
	@echo "🗑 Cleaning up the room..."
	rm -rf essays .venv graham.epub graham.md ; true

merge:
	@echo "🌪 Merging articles..."
	pandoc essays/*.md -o graham.md -f markdown_strict

install:
	$(PKG_MANAGER) install python3

venv:
	@echo "🐍 Creating a safe place for a Python... "
	mkdir -p essays
	python3 -m venv .venv
	$(VENV_ACTIVATE) && pip3 install --upgrade pip setuptools
	$(VENV_ACTIVATE) && pip3 install -r requirements.txt

fetch:
	@echo "🧠 Downloading Paul Graham mind... "
	$(VENV_ACTIVATE) && python3 graham.py

epub: merge
	@echo "📒 Binding EPUB... "
	pandoc essays/*.md -o graham.epub -f markdown_strict --metadata-file=metadata.yaml --toc --toc-depth=1 --epub-cover-image=cover.png
	@echo "🎉 EPUB file created."

pdf: epub
	@echo "📒 Binding PDF... "
	ebook-convert graham.epub graham.pdf
	@echo "🎉 PDF file created."

dependencies:
	if [ "$(UNAME_S)" = "Darwin" ]; then \
		$(PKG_MANAGER) install python pandoc calibre || true; \
	else \
		sudo apt update && sudo apt install -y python3-pip python3-venv pandoc calibre; \
	fi

wordcount:
	@echo "📊 Counting words..."
	@echo "Total words: "
	@cat essays/*.md | wc -w
	@echo "Total articles: "
	@ls essays/*.md | wc -l
