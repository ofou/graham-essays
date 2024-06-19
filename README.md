# Graham Essays Collection
[![CI](https://github.com/ofou/graham-essays/actions/workflows/main.yml/badge.svg)](https://github.com/ofou/graham-essays/actions/workflows/main.yml) [![Ubuntu](https://github.com/ofou/graham-essays/actions/workflows/ubuntu.yml/badge.svg)](https://github.com/ofou/graham-essays/actions/workflows/ubuntu.yml) [![wakatime](https://wakatime.com/badge/github/ofou/graham-essays.svg?style=social)](https://wakatime.com/badge/github/ofou/graham-essays)

![https://startupquote.com/post/3890222281](https://64.media.tumblr.com/tumblr_li4p22jETB1qz6pqio1_500.png)

> "If you are not embarrassed by the first version of your product, you've launched too late".

---

**Check out the [releases page] for the latest build, updated daily.**

Download the _complete collection_ of +200 essays from [Paul Graham] website and export them in [EPUB], and Markdown for easy [AFK] reading. It turned out to be a whooping +500k words. I used the RSS originally made by [Aaron Swartz] [shared] by PG himself, `feedparser`, `html2text`, `htmldate` and `Unidecode` libraries for data cleaning and acquisition. 

## Dependencies for MacOS

On macOS you need [brew] in order to install the dependencies listed in the Makefile.

## Usage

Run the [Makefile](./Makefile) in the root directory using:

```bash
make
```

### Current Essays

Here's a [list] of the current essays included, and an [EPUB].

---

_If you have any ideas, suggestions, curses or feedback in order to improve the code, please don't hesitate in opening an issue or PR. They'll be very welcomed!_

[afk]: https://www.grammarly.com/blog/afk-meaning/
[paul graham]: http://www.paulgraham.com/articles.html
[aaron swartz]: https://en.wikipedia.org/wiki/Aaron_Swartz
[brew]: https://docs.brew.sh/Installation
[pandoc]: https://pandoc.org/installing.html
[calibre]: https://calibre-ebook.com/
[EPUB]: https://github.com/ofou/graham-essays/releases/download/latest/graham.epub
[releases page]: https://github.com/ofou/graham-essays/releases/tag/latest
[shared]: http://www.paulgraham.com/rss.html
[list]: https://github.com/ofou/graham-essays/releases/download/latest/essays.csv
