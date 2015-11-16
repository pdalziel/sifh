from .fixtures import test_file
from libextract.api import extract, pipeline, select, measure, rank, finalise
from goose import Goose


def test_extract(test_file):
    r = extract(test_file)
    u = [node.tag for node in r]
    assert u == [
        'article',
        'body',
    ]


def test_goose_extract(test_file):
    g = Goose
    article = g.extract(raw_html=test_file)
