import feedparser
import urllib.request
import time
import os.path
import html2text
import unidecode

"""
Download full collection of Paul Graham essays in EPUB & Markdown.

Merge all the files using:
    cat essays/*.md > graham.md

Convert to EPUB them using pandoc
    pandoc graham.md -o graham.epub -f gfm --metadata title="Paul Graham Essays"
"""

rss = feedparser.parse("http://www.aaronsw.com/2002/feeds/pgessays.rss")
h = html2text.HTML2Text()
h.ignore_images = True
h.ignore_tables = True
h.escape_all = True
h.reference_links = True
h.mark_code = False

art_no = 1

for entry in reversed(rss.entries):
    url = entry['link']
    opener = urllib.request.FancyURLopener({})

    try:
        with opener.open(url) as website:
            content = website.read().decode('unicode_escape', "utf-8")
            parsed = h.handle(content)
            title = entry['title'].strip("/")
            with open(f"./essays/{art_no:03}_{title}.md", 'wb+') as file:
                file.write(parsed.encode())
                print(f"✅ {art_no:03} {entry['title']}")

    except Exception as e:
        print(f"❌ {art_no:03} {entry['title']}, ({e})")
    art_no += 1
    time.sleep(1)  # 1s per article is ~4min, be nice with servers!
