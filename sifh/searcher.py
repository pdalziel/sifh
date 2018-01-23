from whoosh import index
from whoosh.qparser import QueryParser

path = "../clef_small_sample/"  # local path to single desktop file
# path = u"../clef2015/" #local path to desktop files
# path = u"../clef2015-problemfiles/"

idx_name = path[3:-1]
print idx_name

path_to_index = "./index"
ix = index.open_dir(path_to_index, indexname=idx_name)

# searcher = ix.searcher()
qp = QueryParser("content", schema=ix.schema)
q = qp.parse(u"health")

with ix.searcher() as searcher:
    results = searcher.search(q, terms=True)
    if len(results) > 0:
        for hit in results:
            print(hit["docid"])
            print(hit["title"])
            print(hit.highlights("content"))
    else:
        print "no hits"

path = "../clef_small_sample/"  # local path to single desktop file
# path = u"../clef2015/" #local path to desktop files
# path = u"../clef2015-problemfiles/"

idx_name = path[3:-1]
print idx_name

path_to_index = "./index"
ix = index.open_dir(path_to_index, indexname=idx_name)

# searcher = ix.searcher()
qp = QueryParser("content", schema=ix.schema)
q = qp.parse(u"health")

with ix.searcher() as searcher:
    results = searcher.search(q, terms=True)
    if len(results) > 0:
        for hit in results:
            print("docid:", hit["docid"])
            print("title:", hit["title"])
            print("content:", hit.highlights("content"))
    else:
        print "no hits"
