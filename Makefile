SHELL := /bin/bash

.SILENT: clean venv fetch merge epub words count mobi

all:  	dependencies clean venv fetch merge epub mobi pdf

clean: 
		@echo "🗑 Cleaning up the room..."
		rm -rf essays .venv graham.epub graham.md ; true

merge:
		@echo "🌪 Merging articles..."
		pandoc essays/*.md -o graham.md -f markdown_strict

count:	
		wc -w essays/* | sort -n

install:
		brew install python3

venv:
		@echo "🐍 Creating a safe place for a Python... "
		mkdir essays
		python3 -m venv .venv
		source "./.venv/bin/activate"
		pip3 install --upgrade pip
		pip3 install -r requirements.txt

dependencies: # for MacOS
		brew install python
		brew install --build-from-source pandoc
		brew install --cask calibre

fetch:	
		@echo "🧠 Downloading Paul Graham mind... "
		python3 graham.py 

epub:
		${merge}
		@echo "📒 Binding EPUB... "
		pandoc essays/*.md -o graham.epub -f markdown_strict --metadata-file=metadata.yaml --toc --toc-depth=1 --epub-cover-image=cover.png
		@echo "🎉 EPUB file created."

pdf:
		${epub}
		@echo "📒 Binding PDF... "
		ebook-convert graham.epub graham.pdf
		@echo "🎉 PDF file created."
