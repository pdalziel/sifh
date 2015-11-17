import os
import os.path
import sys
import logging

from whoosh import index
from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, TEXT, ID

from bs4 import BeautifulSoup
from goose import Goose
from libextract.api import extract

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(filename='sifh.log', level=logging.DEBUG)
log = logging.getLogger('logger')

stemmer = StemmingAnalyzer()
schema = Schema(docid=TEXT(stored=True),
                title=TEXT(analyzer=stemmer, stored=True),
                content=TEXT(analyzer=stemmer, stored=True),
                timedate=TEXT(stored=True),
                source=TEXT(stored=True),
                alltext=TEXT(stored=True))


ix = create_in("index", schema)
writer = ix.writer()
path = "./clef_small_sample/" #local path to single desktop file
# path = "./clef2015-sample/" #local path to desktop files


def make_file_list():
    html_files = os.listdir(path)
    log.debug(html_files)
    return html_files


def mkdir_index():
    if not os.path.exists("index"):
        log.info('creating index')
        os.mkdir("index")


def create_index():
    html_files = make_file_list()
    for html_file in html_files:
        ndocid = unicode(html_file)
        html = open(path + html_file, 'r').read()
        nalltext = extract_all_text(html)
        article = goose_extract(html)
        ncontent = extract_main_text(article)
        ntitle = extract_title(article)
        writer.add_document(docid=ndocid, title=ntitle, content=ncontent, alltext=nalltext)
        log.info('added ' + ndocid)
    writer.commit()


def extract_main_text(article):
    return article.cleaned_text


def extract_title(article):
    if article.title is not None:
            title = article.title
    return title


def extract_all_text(html):
    textnodes = list(extract(html))
    text_str = ''.join((e.text_content().encode('utf-8')) for e in textnodes)
    return unicode(text_str.strip('  '))


def goose_extract(html):
    g = Goose()
    article = g.extract(raw_html=html)
    log.debug(article)
    return article


def main(argv):
    mkdir_index()
    create_index()

if __name__ == "__main__":
    main(sys.argv)