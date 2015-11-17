import os
import os.path


from whoosh import query
from whoosh import index
from whoosh import searching
from whoosh.qparser import QueryParser

path_to_index = "./index"
ix = index.open_dir(path_to_index)

searcher = ix.searcher()
qp = QueryParser("title", schema=ix.schema)
q = qp.parse(u"health")

with ix.searcher() as searcher:
    results = searcher.search(q)
    print "finished"
    for r in results:
        print r