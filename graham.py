from asyncio.log import logger
import feedparser
import urllib.request
import time
import os.path
import html2text
import unidecode
import regex as re
from htmldate import find_date

"""
Download a collection of Paul Graham essays in EPUB & Markdown.
"""

rss = feedparser.parse("http://www.aaronsw.com/2002/feeds/pgessays.rss")
h = html2text.HTML2Text()
h.ignore_images = True
h.ignore_tables = True
h.escape_all = True
h.reference_links = True
h.mark_code = True

art_no = 1
FILE = "./essays.csv"

if art_no == 1:
    # remove existing file
    if os.path.isfile(FILE):
        os.remove(FILE)

for entry in reversed(rss.entries):
    url = entry['link']

    try:
        with urllib.request.urlopen(url) as website:
            content = website.read().decode('unicode_escape', "utf-8")
            parsed = h.handle(content)
            title = "_".join(entry['title'].split(" ")).lower()
            title = re.sub(r'[\W\s]+', '', title)
            with open(f"./essays/{art_no:03}_{title}.md", 'wb+') as file:
                file.write(f"# {art_no:03} {entry['title']}\n\n".encode())
                parsed = parsed.replace("[](index.html)  \n  \n", "")

                parsed = [(p.replace("\n", " ")
                          if re.match(r"^[\p{Z}\s]*(?:[^\p{Z}\s][\p{Z}\s]*){5,100}$", p)
                          else "\n"+p+"\n") for p in parsed.split("\n")]

                file.write(" ".join(parsed).encode())
                print(f"✅ {art_no:03} {entry['title']}")

                with open(FILE, 'a+') as csv:
                    if art_no == 1:
                        csv.write(f"Article No., Title, Date, URL \n")
                    date = find_date(
                        entry['link'], original_date=True, extensive_search=True)
                    title = entry['title'].replace("\"", "'")
                    csv.write(
                        f"{art_no:03},{title},{date},{entry['link']}\n")
                    # print(entry)

    except Exception as e:
        print(f"❌ {art_no:03} {entry['title']}, ({e})")
    art_no += 1
    time.sleep(0.05)  # half sec/article is ~2min, be nice with servers!
