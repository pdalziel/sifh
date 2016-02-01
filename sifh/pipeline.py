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
operator = "OrGroup"
q = query_parser.QueryGenerator()
list_of_queryies = QueryGenerator.parse_queries(q, fieldname, operator, myindex)


for i in range(1, 10, 1):
    sr = SearchRunner(i/10.0)
    run_id = "BASELINE_RUN_" + str(i)
    sr.run_search(list_of_queryies, run_id)


# read settings for run
# send instructions to searcher
# searcher calls query parser to generate queries
# searcher outputs results file

# pass results anc qrels to trec
# then collect and collate trec results
# genrate graphs from trec results