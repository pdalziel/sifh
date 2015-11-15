import os
import os.path


from requests import get
from libextract.api import extract

r = get('')
textnodes = list(extract(r.content))

for node in textnodes:
    print node.text_content()