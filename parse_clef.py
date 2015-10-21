import os
import os.path

from bs4 import BeautifulSoup

from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import *

#path = "./clef_small_sample/" #local path to single desktop file
path = "./clef2015-sample/" #local path to desktop files
html_files = os.listdir(path)
stemmer = StemmingAnalyzer()

schema = Schema(docid=TEXT(stored=True),
                title=TEXT(analyzer=stemmer, stored=True),
                content=TEXT(analyzer=stemmer, stored=True),
                timedate=TEXT(stored=True),
                source=TEXT(stored=True),
                alltext=TEXT(stored=True))


def parse_clef_files(html_file):
    soup = BeautifulSoup(open(html_file, 'r').read(), "lxml")
    ndocid = html_file
    print ndocid
    if soup.source is not None:
        print "\n source = " + soup.source
    if soup.title is not None:
        ntitle = soup.title.string
        print "title = " + ntitle
    else:
        print " \n " + ndocid+ "HAS NO TITLE! \n"

    nalltext = soup.find_all(text=True)

    print nalltext


for html_file in html_files:

    parse_clef_files(path+html_file)
    print "NEXT FILE\n"


