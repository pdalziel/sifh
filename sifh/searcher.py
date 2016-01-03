import os
import os.path
import xml.etree.ElementTree as ET
import logging

from whoosh import query
from whoosh import index
from whoosh import searching
from whoosh.qparser import QueryParser

#path = u"./clef_small_sample/" #local path to single desktop file
path = "../clef2015/" #local path to desktop files
#path = u"../clef2015-problemfiles/"



idx_name = path[3:-1]
queries_path = "/home/paul/Project/sifh/queries/clef2015.training.queries-EN.txt" # "/home/paul/Project/sifh/queries/clef2015.test.queries-EN.txt"
logging.basicConfig(filename='searcher.log', level=logging.INFO)
log = logging.getLogger('logger')
path_to_index = "/home/paul/Project/sifh/index"
ix = index.open_dir(path_to_index)

qp = QueryParser("content", schema=ix.schema)

tree = ET.parse(queries_path)
root = tree.getroot()

for q in root.findall('top'):
    query = q.find('query').text
    q = qp.parse(unicode(query))
    with ix.searcher() as searcher:
        results = searcher.search(q, terms=True)
        #log.info(str(len(results)) + " hits")
        log.info(query)
        print query
        for hit in results:
                log.info(u"TITLE: " + (hit["title"]) + u" DOCID: " + (hit["docid"]) + u" SCORE:  " + unicode(hit.score))
                print (u"TITLE: " + (hit["title"]) + u" DOCID: " + (hit["docid"]) + u" SCORE: " + unicode(hit.score))