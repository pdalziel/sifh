import os
import os.path

from bs4 import BeautifulSoup

from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import *

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


def parse_clef_files(html_file):
    ndocid = html_file
    soup = BeautifulSoup(open(path+html_file, 'r').read(), "lxml")
    print ndocid
    if soup.source is not None:
        print "\n source = "
        print soup.source
    if soup.title is not None:
        ntitle = soup.title.string
        print ntitle
    if soup.find({""}) is not None:
        print soup.timedate
    ncontent = soup.findAll(text=True)
    print ncontent
    nalltext = soup.get_text()


for html_file in html_files:
    parse_clef_files(html_file)
    print "NEXT FILE\n"


