import os
import os.path
import xml.etree.ElementTree as ET
import logging

from whoosh import query
from whoosh import index
from whoosh import searching
from whoosh.qparser import QueryParser

# path = u"./clef_small_sample/" #local path to single desktop file

path = "../clef2015/"  # local path to desktop files
# path = u"../clef2015-problemfiles/"

res_file = "./res_file.txt"

idx_name = path[3:-1]
queries_path = "/home/paul/Project/sifh/queries/clef2015.test.queries-EN.txt"

logging.basicConfig(filename='searcher.log', level=logging.INFO)
log = logging.getLogger('logger')
path_to_index = "/home/paul/Project/sifh/index"
ix = index.open_dir(path_to_index)

qp = QueryParser("content", schema=ix.schema)
# f = open(queries_path)

tree = ET.parse(queries_path)
root = tree.getroot()
itr = " 0 "
run_id = " base "
rank = " 0 "


def create_results_flie(qid, docid, sim):
    with open(res_file, 'a') as result_file:
        pass
        result_file.write(str(qid + itr + docid + rank + sim + run_id + "\n"))
        # print (str(qid + itr + docid + rank + sim + run_id + "\n"))


for q in root.findall('top'):
    # print q
    query = q.find('query').text
    qid = str(q.find('num').text)
    q = qp.parse(unicode(query))
    with ix.searcher() as searcher:
        results = searcher.search(q, limit=None)
        # log.info(str(len(results)) + " hits")
        log.info(query)
        #print query

        #print results.__len__()
        for hit in results:
            if results.has_matched_terms:
                sim = str(hit.score)
            else:
                sim = "0"
            docid = str(hit["docid"])
            create_results_flie(qid, docid, sim)
            # log.info(u"TITLE: " + (hit["title"]) + u" DOCID: " + (hit["docid"]) + u" SCORE:  " + unicode(hit.score))
            # print (hit.matched_terms())
            # print (u"TITLE: " + (hit["title"]) + u" DOCID: " + (hit["docid"]) + (hit["meta_tag_contents"]) + u" SCORE: " + unicode(hit.score))
