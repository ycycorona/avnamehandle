class Proxy(object):
    def __init__(self, proxy_url):
        self.proxy_url = proxy_url

    def get_proxy(self):
        return {
            'http': self.proxy_url,
            'https': self.proxy_url
        }
