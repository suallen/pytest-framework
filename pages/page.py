class Page(object):

    _url = None

    def __init__(self, base_url, selenium):
        self.base_url = base_url
        self.selenium = selenium

    def open(self):
        self.selenium.get(self.url)
        self.wait_for_page_to_load()
        return self

    @property
    def url(self):
        if self._url is not None:
            return self._url.format(base_url=self.base_url)
        return self.base_url

    def wait_for_page_to_load(self):
        return self