import os
import os.path


from whoosh import query
from whoosh import index
from whoosh import searching
from whoosh.qparser import QueryParser

#path = u"./clef_small_sample/" #local path to single desktop file
#path = u"../clef2015/" #local path to desktop files
path = u"../clef2015-problemfiles/"

idx_name = path[3:-1]


path_to_index = "/home/paul/Project/sifh/index"
ix = index.open_dir(path_to_index, indexname=idx_name)

#searcher = ix.searcher()
qp = QueryParser("content", schema=ix.schema)
q = qp.parse(u"psychotherapy")

with ix.searcher() as searcher:
    results = searcher.search(q, terms=True)
    for hit in results:
        print(hit["title"])
        print(hit.highlights("content"))
