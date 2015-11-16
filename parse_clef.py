import os
import os.path
import codecs

from bs4 import BeautifulSoup
from goose import Goose
from libextract.api import extract

from whoosh import index
from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, TEXT, ID

path = "./clef_small_sample/" #local path to single desktop file
#path = "./clef2015-sample/" #local path to desktop files
html_files = os.listdir(path)

stemmer = StemmingAnalyzer()
schema = Schema(docid=TEXT(stored=True),
                title=TEXT(analyzer=stemmer, stored=True),
                content=TEXT(analyzer=stemmer, stored=True),
                timedate=TEXT(stored=True),
                source=TEXT(stored=True),
                alltext=TEXT(stored=True))

ix = create_in("index", schema)
writer = ix.writer()

if not os.path.exists("index"):
    os.mkdir("index")


def create_index():
    for html_file in html_files:
        ndocid = html_file
        with codecs.open(path+html_file, 'r', "utf-8") as f:
            html = f.read()
            g = Goose()
            article = g.extract(raw_html=html)
            ncontent = article.cleaned_text
            if article.title is not None:
                ntitle = article.title
            nalltext = extract_all_text(html)
            writer.add_document(docid=ndocid, title=ntitle, content=ncontent, alltext=nalltext)
    writer.commit()


def extract_all_text(html):
    textnodes = list(extract(html))
    text_str = ''.join(str(e.text_content()) for e in textnodes)
    return text_str

create_index()
