import os
import os.path


from whoosh import query
from whoosh import index
from whoosh import searching
from whoosh.qparser import QueryParser

path_to_index = "./index"
ix = index.open_dir(path_to_index)

searcher = ix.searcher()
qp = QueryParser("content", schema=ix.schema)
q = qp.parse(u"doctor")

with ix.searcher() as searcher:
    results = searcher.search(q)
    for r in results:
        print r