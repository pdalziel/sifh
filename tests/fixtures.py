import pytest
from libextract.api import extract
from goose import Goose

from tests import asset_path

TEST_FILENAME = asset_path('test_file')


@pytest.fixture
def foo_file(request):
    fp = open(TEST_FILENAME, 'rb')
    request.addfinalizer(fp.close)
    return fp
