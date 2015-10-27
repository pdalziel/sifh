import os
import os.path

from bs4 import BeautifulSoup

from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import *

path = "./clef_small_sample/" #local path to single desktop file
#path = "./clef2015-sample/" #local path to desktop files
html_files = os.listdir(path)
stemmer = StemmingAnalyzer()

schema = Schema(docid=TEXT(stored=True), title=TEXT(analyzer=stemmer, stored=True), content=TEXT(analyzer=stemmer, stored=True), timedate=TEXT(stored=True), source=TEXT(stored=True), alltext=TEXT(stored=True) )


def parse_data_files(from_folder=None):
	record_buffer = 2 * 1024
	if not from_folder or not os.path.exists(from_folder):
		# yeild no results if no folder given or does not exist
		yield None

	else:
		# iterate over all files in directory
		for f in os.listdir(from_folder)
		#create path
		fp=os.path.join(from_folder, f)
		with open(fp, 'r') as ins_file:
			while True:
                data=ins_file.read(record_buffer)
                if not data:
                    break
                    yeild(f, data)

records=parse_data_files('r'.clef2015_sample)

# create a unicode helper function
_u = lambda s: unicode(s, encoding='latin1')

writer=idx.writer()

for index, record in enumerate(records):
	book, contents=record



 kwrds = ' '.join([_u(word) for word, cnt in kwrds])

    # write the document to the index
    writer.add_document(
        uuid = _u(str(uuid.uuid4())),
        title = _u(book),
        content = _u(contents),
        page = index,
        keywords = kwrds
    )

     # commit every 100 records
    if index % 100 == 0:
        # we want to index as fast as possible and not
        # spend too much time merging segments. At
        # the end of writing all the records we call
        # an optimized commit that will take all of our
        # micro segments and combine them into one big
        # table.
        writer.commit(merge=False)

        # re-instantiate the writer
        writer = idx.writer()

# do an optimized commit for the remaining records
writer.commit(optimize=True)
