import urllib.request
from urllib.parse import urljoin
import time
import os.path
import html2text
import regex as re
from htmldate import find_date
import csv
import requests
from bs4 import BeautifulSoup

"""
Download a collection of Paul Graham essays in EPUB & Markdown.
"""

h = html2text.HTML2Text()
h.ignore_images = True
h.ignore_tables = True
h.escape_all = True
h.reference_links = True
h.mark_code = True

ART_NO = 0
FILE = "./essays.csv"

if os.path.isfile(FILE):
    os.remove(FILE)


def parse_main_page(base_url: str, articles_url: str):
    assert base_url.endswith("/"), f"Base URL must end with a slash: {base_url}"
    response = requests.get(base_url + articles_url)
    soup = BeautifulSoup(response.text, "html.parser")

    td_cells = soup.select("table > tr > td > table > tr > td")
    chapter_links = []

    for td in td_cells:
        img = td.find("img")
        if img and int(img.get("width", 0)) <= 15 and int(img.get("height", 0)) <= 15:
            a_tag = td.find("font").find("a") if td.find("font") else None
            if a_tag:
                chapter_links.append(
                    {"link": urljoin(base_url, a_tag["href"]), "title": a_tag.text}
                )

    return chapter_links


toc = list(reversed(parse_main_page("https://paulgraham.com/", "articles.html")))


def convert_to_pandoc_footnotes(text, essay_id=""):
    if isinstance(text, bytes):
        text = text.decode("utf-8")

    notes_section_pattern = r"\*\*Notes?\*\*.*?(?=\n\s*\*\*|\Z)"
    notes_match = re.search(notes_section_pattern, text, re.DOTALL | re.IGNORECASE)

    if not notes_match:
        return text.encode("utf-8")

    notes_content = notes_match.group(0)

    footnote_pattern = r"\[(\d+)\]\s*(.*?)(?=\s*\[\d+\]|\s*$)"
    footnotes = re.findall(footnote_pattern, notes_content, re.DOTALL)

    if not footnotes:
        return text.encode("utf-8")

    footnote_definitions = {}
    for note_num, note_content in footnotes:
        note_content = note_content.strip()
        note_content = re.sub(r"\s+", " ", note_content)
        note_content = note_content.strip()

        if note_content:
            footnote_definitions[note_num] = note_content

    text = re.sub(notes_section_pattern, "", text, flags=re.DOTALL | re.IGNORECASE)

    prefix = f"{essay_id}-" if essay_id else ""
    for note_num in footnote_definitions.keys():
        text = re.sub(rf"\[{note_num}\]", f"[^{prefix}{note_num}]", text)

    if footnote_definitions:
        footnote_defs = []
        for note_num in sorted(footnote_definitions.keys(), key=int):
            footnote_content = footnote_definitions[note_num]
            footnote_defs.append(f"[^{prefix}{note_num}]: {footnote_content}")

        text += "\n\n" + "\n\n".join(footnote_defs)

    return text.encode("utf-8")


with open(FILE, "a+", newline="\n") as f:
    fieldnames = ["Article no.", "Title", "Date", "URL"]
    csvwriter = csv.DictWriter(f, fieldnames=fieldnames)
    csvwriter.writeheader()

for entry in toc:
    ART_NO += 1
    URL = entry["link"]
    if "http://www.paulgraham.com/https://" in URL:
        URL = URL.replace("http://www.paulgraham.com/https://", "https://")
    TITLE = entry["title"]

    try:
        try:
            with urllib.request.urlopen(URL) as website:
                content = website.read().decode("utf-8")
        except UnicodeDecodeError:
            with urllib.request.urlopen(URL) as website:
                content = website.read().decode("latin-1")

        parsed = h.handle(content)
        title = "_".join(TITLE.split(" ")).lower()
        title = re.sub(r"[\W\s]+", "", title)

        pg_date_match = re.search(
            r"<font[^>]*>((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})",
            content,
            re.IGNORECASE,
        )
        if pg_date_match:
            from dateparser import parse

            date_str = pg_date_match.group(1)
            parsed_date = parse(date_str)
            if parsed_date:
                DATE = parsed_date.strftime("%Y-%m-%d")
            else:
                DATE = find_date(content)
        else:
            DATE = find_date(content)
        with open(f"./essays/{str(ART_NO).zfill(3)}_{title}.md", "wb+") as file:
            file.write(f"# {str(ART_NO).zfill(3)} {TITLE}\n\n".encode())
            parsed = parsed.replace("[](index.html)  \n  \n", "")

            parsed = [
                (
                    p.replace("\n", " ")
                    if re.match(r"^[\p{Z}\s]*(?:[^\p{Z}\s][\p{Z}\s]*){5,100}$", p)
                    else "\n" + p + "\n"
                )
                for p in parsed.split("\n")
            ]

            encoded = " ".join(parsed).encode()
            processed_content = convert_to_pandoc_footnotes(encoded, str(ART_NO).zfill(3))
            file.write(processed_content)

            print(f"✅ {str(ART_NO).zfill(3)} {TITLE}")

            with open(FILE, "a+", newline="\n") as f:
                csvwriter = csv.writer(
                    f, quoting=csv.QUOTE_MINIMAL, delimiter=",", quotechar='"'
                )

                line = [str(ART_NO).zfill(3), TITLE, DATE, URL]

                csvwriter.writerow(line)

    except Exception as e:
        print(f"❌ {str(ART_NO).zfill(3)} {entry['title']}, ({e})")
    time.sleep(0.05)  # half sec/article is ~2min, be nice with servers!
