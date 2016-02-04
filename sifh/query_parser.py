import os
import os.path
import xml.etree.ElementTree as ET
import logging

from whoosh import query
from whoosh import index
from whoosh import searching
from whoosh import qparser



class QueryGenerator(object):

        def parse_queries(self, fields, operator, myindex):
            self.fields = fields
            self.operator = operator
            path_to_index = "/home/paul/Project/sifh/index"
            self.myindex = index.open_dir(path_to_index)
            queries_path = "/home/paul/Project/sifh/queries/clef2015.test.queries-EN.txt"
            tree = ET.parse(queries_path)
            root = tree.getroot()
            query_l = []
            if operator == "OR":
                parser = qparser.QueryParser(self.fields[0], schema=self.myindex.schema, group=qparser.OrGroup)
            else:
                parser = qparser.QueryParser(self.fields[0], schema=self.myindex.schema)
            for q in root.findall('top'):
                query_str = q.find('query').text
                qid = str(q.find('num').text)
                qp = parser.parse(unicode(query_str))
                query_l.append([qid, query_str])
            return query_l

