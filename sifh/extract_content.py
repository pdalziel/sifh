from bs4 import BeautifulSoup


class HtmlSoup:
    def __init__(self, html):
        self.soup = BeautifulSoup(html)

    def get_title(self):
        if self.soup.title is not None:
                title = self.soup.title.string
        else:
            title = u"None"
        return title

    def get_meta_contents(self):
        if self.soup.find_all('meta') is not None:
            meta = self.soup.find_all('meta')
        else:
            meta = u"None"
        return meta

    def extract_all_text(self):
        return self.soup.find_all()






