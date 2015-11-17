import os
import os.path

from libextract.api import extract
from goose import Goose

import nltk


path = "./clef_small_sample/" #local path to single desktop file
#path = "./clef2015-sample/" #local path to desktop files
file_list = os.listdir(path)
for f in file_list:
    html = open(path+f, 'r').read()
    g = Goose()
    article = g.extract(raw_html=html)
    # print article.cleaned_text
    textnodes = list(extract(html))
    text_str = ''.join((e.text_content().encode('utf-8')) for e in textnodes)
    print text_str
