import os
import os.path


from bs4 import BeautifulSoup
from goose import Goose
from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import *

path = u"./clef_small_sample/" #local path to single desktop file
#path = "./clef2015-sample/" #local path to desktop files
html_files = os.listdir(path)
stemmer = StemmingAnalyzer()

schema = Schema(docid=TEXT(stored=True),
                title=TEXT(analyzer=stemmer, stored=True),
                content=TEXT(analyzer=stemmer, stored=True),
                timedate=TEXT(stored=True),
                source=TEXT(stored=True),
                alltext=TEXT(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")

# whoosh variables
ix = create_in("index", schema)
writer = ix.writer()


def parse_files(html_file):
    ndocid = html_file
    soup = BeautifulSoup(open(path+html_file, 'r').read(), "lxml")
    print soup
    if soup.title is not None:
        ntitle = soup.title.string

    #[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    ncontent = extract_content_block(soup)
    nalltext = ntitle + ncontent
    print nalltext
    writer.add_document(docid=ndocid, title=ntitle, content=ncontent, alltext=nalltext)


def create_index():
    for html_file in html_files:
        #parse_files(html_file)
        extract_content_block(html_file)
    #writer.commit()


def extract_content_block(html_file):
    g = Goose()
    url = path+html_file
    print url
    article = g.extract(url=url)
    content_block = article.cleaned_text[:150]
    print content_block

create_index()


