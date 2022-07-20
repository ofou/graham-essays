# Graham Essays Collection
[![CI](https://github.com/ofou/graham-essays/actions/workflows/main.yml/badge.svg)](https://github.com/ofou/graham-essays/actions/workflows/main.yml) [![Ubuntu](https://github.com/ofou/graham-essays/actions/workflows/ubuntu.yml/badge.svg)](https://github.com/ofou/graham-essays/actions/workflows/ubuntu.yml)

![https://startupquote.com/post/3890222281](https://64.media.tumblr.com/tumblr_li4p22jETB1qz6pqio1_500.png)

> **Alert**: This is a MVP and still a work-in-progress but I wanted to share my current implementation. Sorry if too messy, but following the very YC advise: _"If you are not embarrassed by the first version of your product, you've launched too late"_.

---

Download the _complete collection_ of [+200](essays.csv) essays from [Paul Graham] website and export them in [EPUB], [MOBI] and Markdown for easy [AFK] reading. It turned out to be a whooping +500k words. I used the RSS originally made by [Aaron Swartz], `feedparser`, `html2text`, `htmldate` and `Unidecode` libraries for data cleaning and acquisition. 

Check out the [releases page] for the latest build, updated daily.

## Dependencies for MacOS

To create the EPUB/MOBI files you should have installed [python3], [pandoc] and [calibre] for Kindle readers.

```bash
brew install python@3
brew install --build-from-source pandoc
brew install --cask calibre
```

## Usage

Run the [Makefile](./Makefile) in the root directory using `make all`.

https://github.com/ofou/graham-essays/blob/80249f949235c56c87479bdfd4f32063266d3527/Makefile#L5-L45

### Current Essays

Here's a [list](./essays.csv) of the current essays included.

---

_If you have any ideas, suggestions, curses or feedback in order to improve the code, please don't hesitate in opening an issue or PR. They'll be very welcomed!_

[afk]: https://www.grammarly.com/blog/afk-meaning/
[paul graham]: http://www.paulgraham.com/articles.html
[aaron swartz]: https://en.wikipedia.org/wiki/Aaron_Swartz
[python3]: https://www.python.org/downloads
[pandoc]: https://pandoc.org/installing.html
[calibre]: https://calibre-ebook.com/
[EPUB]: https://github.com/ofou/graham-essays/releases/download/latest/graham.epub
[MOBI]: https://github.com/ofou/graham-essays/releases/download/latest/graham.mobi
[releases page]: https://github.com/ofou/graham-essays/releases/tag/latest