import os
import os.path
import xml.etree.ElementTree as ET
import logging
import query_parser

from whoosh.qparser import QueryParser
from whoosh import index
from whoosh import searching
from whoosh import scoring


class SearchRunner(object):

    def __init__(self, variable):
        #self.algorithm = algorithm
        self.variable = variable

    def gen_results_file_name(self, w, run_id):
        runname = "BM25F.B=" + str(self.variable) + "_" + run_id + ".dat"
        return runname

    def output_results(self, w, qid, docid, rank, sim, run_id):
        itr = " Q0 "
        filename = self.gen_results_file_name(w, run_id)
        with open(filename, 'a') as result_file:
            ranking = str(rank)
            result_file.write(str(qid + itr + docid + " " + ranking + " " + sim + " " + run_id + "\n"))

    def run_search(self, query_list, run_id):
        w = scoring.BM25F(B=self.variable)
        path_to_index = "/home/paul/Project/sifh/index"
        ix = index.open_dir(path_to_index)
        qp = QueryParser("content", schema=ix.schema)
        for q in query_list:
            qid = q[0]
            q_str = q[1]
            query = qp.parse(unicode(q_str))
            with ix.searcher(weighting=w) as searcher:
                results = searcher.search(query, limit=None)
                rank = 0
                for hit in results:
                    rank += 1
                    if results.has_matched_terms:
                        sim = str(hit.score)
                    else:
                        sim = "0"
                    docid = str(hit["docid"])
                    self.output_results(w, qid, docid, rank, sim, run_id)

        print str(w.B) + " finished"



