import os
import os.path
import sys
import logging
import codecs
import whoosh.index as index

from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, TEXT

from sifh.extract_content import HtmlSoup
from sifh.libextract_text import extract_visable_text

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(filename='sifh.log', level=logging.DEBUG)
log = logging.getLogger('logger')

stemmer = StemmingAnalyzer()
schema = Schema(docid=TEXT(stored=True),
                title=TEXT(analyzer=stemmer, stored=True),
                content=TEXT(analyzer=stemmer, stored=True),
                timedate=TEXT(stored=True),
                meta_tag_contents=TEXT(stored=True),
                alltext=TEXT(stored=True))



path = u"../clef_small_sample/" #local path to single desktop file
#path = u"../clef2015/" #local path to desktop files
#path = u"../clef2015-problemfiles/"

idx_name = path[3:-1]
print idx_name


if not os.path.exists("index"):
    log.info('created index folder')
    os.mkdir("index")

if index.exists_in("index", indexname=idx_name):
     log.info('found index')
     ix = index.open_dir("index", indexname=idx_name)

else:
    log.info('created index' + "idx_name")
    ix = create_in("index", schema=schema, indexname=idx_name)


def make_file_list():
    html_files = os.listdir(path)
    log.debug(html_files)
    return html_files


def create_index():
    writer = ix.writer()
    html_files = make_file_list()
    count = len(html_files)
    for html_file in html_files:
        ndocid = html_file
        file_path = path + html_file
        html = codecs.open(file_path,  encoding='utf-8').read()
        soup = HtmlSoup(html)
        ntitle = soup.get_title()
        #nall_text = soup.extract_all_text()
        nmeta = soup.get_meta_contents()
        ncontent = extract_visable_text(file_path)
        #print ncontent
        writer.add_document(docid=unicode(ndocid), title=unicode(ntitle),
                            content=unicode(ncontent), meta_tag_contents=unicode(nmeta))
        print 'added ' + ndocid
        count -= 1
        print count
        log.info('added ' + ndocid)

    writer.commit()


def main(argv):
    create_index()

if __name__ == "__main__":
    main(sys.argv)