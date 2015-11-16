import os
import os.path

from libextract.api import extract
from goose import Goose

import nltk


path = "./clef_small_sample/yourh5013_12_020483" #local path to single desktop file
#path = "./clef2015-sample/" #local path to desktop files
html = open(path,'r').read()

g = Goose()
article = g.extract(raw_html=html)

print article.cleaned_text

textnodes = list(extract(html))
i=0
for node in textnodes:
    print str(i) + " " + node.text_content()
    i += 1
