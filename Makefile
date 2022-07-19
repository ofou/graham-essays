SHELL := /bin/bash

.SILENT: dependencies clean venv fetch merge epub words count mobi

all:  	clean venv fetch merge epub mobi

clean: 
		@echo "🗑 Cleaning up the room..."
		rm -rf essays .venv graham.epub graham.md ; true

merge:
		@echo "🌪 Merging articles..."
		pandoc essays/*.md -o graham.md -f markdown_strict

count:	
		wc -w essays/* | sort -n

venv:
		@echo "🐍 Creating a safe place for a Python... "
		mkdir essays
		python3 -m venv .venv
		source ".venv/bin/activate"
		pip install --upgrade pip
		pip install -r requirements.txt

dependencies: # for MacOS
		brew install python@3
		brew install --build-from-source pandoc
		brew install --cask calibre

fetch:	
		@echo "🧠 Downloading Paul Graham mind... "
		python graham.py 

epub:
		${merge}
		@echo "📒 Binding the EPUB... "
		pandoc essays/*.md -o graham.epub -f markdown_strict --metadata-file=metadata.yaml --toc --toc-depth=1 --epub-cover-image=cover.png
		@echo "🎉 EPUB file created."

mobi:
		${epub}
		@echo "📒 Binding the MOBI... "
		ebook-convert graham.epub graham.mobi
		@echo "🎉 MOBI file created."
