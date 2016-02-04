#!/usr/bin/env python
import os
import ConfigParser
import query_parser

from search_runner import SearchRunner

from query_parser import QueryGenerator
from whoosh.qparser import QueryParser

path = "../clef2015/"
config = ConfigParser.ConfigParser()
config.read("/home/paul/Project/sifh/sifh/config.cnf")
fieldname = ["content"]
myindex = path[3:-1]
operator = "OR"
q = query_parser.QueryGenerator()
list_of_queries = QueryGenerator.parse_queries(q, fieldname, operator, myindex)


for i in range(2, 22, 2):
    sr = SearchRunner(i/10.0)
    run_id = "BASELINE_RUN_OR_" + str(i) + "PL2_c=" + str(i/10.0)
    sr.run_search(list_of_queries, run_id)


# read settings for run
# send instructions to searcher
# searcher calls query parser to generate queries
# searcher outputs results file
# BM25 implicit AND, b=0.1 to b=0.9 done
# BM25 implicit OR, b=0.1 to b=0.9,done
# PL2  implicit OR, c=0.1 to c=2.0 done
# PL2  implicit AND c=0.1 to c=2.0 done
# TFIDF implicit AND done
# TFIDF implicit OR done
# pass results anc qrels to trec
# then collect and collate trec results
# genrate graphs from trec results