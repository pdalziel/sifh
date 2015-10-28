import os
import os.path
import unittest

from bs4 import BeautifulSoup

from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import *
from whoosh.query import *
from whoosh.qparser import QueryParser

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

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# whoosh variables
ix = create_in("indexdir", schema)
writer = ix.writer()
searcher = ix.searcher()
qp = QueryParser("content", schema=ix.schema)
q = qp.parse(u" ")

def parse_files(html_file):
    schema.docid = html_file
    soup = BeautifulSoup(open(path+html_file, 'r').read(), "lxml")
    if soup.title is not None:
        schema.title = soup.title.string
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    schema.content = soup.getText()
    schema.alltext = schema.title + schema.content


def create_index():
    for html_file in html_files:
        parse_files(html_file)
        print schema
        writer.add_document(schema)

writer.commit(optimize=True)

with ix.searcher() as searcher:
    results = searcher.search(q)
    print len(results)