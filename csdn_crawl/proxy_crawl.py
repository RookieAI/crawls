import config as cfg

import requests
from bs4 import BeautifulSoup


class ProxyCrawl:
    def __init__(self, page=0):
        self.user_agent = cfg.OWN_USER_AGENT
        self.proxy_url = cfg.PROXY_URL
        self.page = page

    def get_proxy(self):
        html = requests.get(self.proxy_url + str(self.page)).text
        soup = BeautifulSoup(html, 'html.parser')
        proxy_list = []
        for tr in soup.find_all('tr'):
            ip = tr.find('td', attrs={'data-title': 'IP'})
            port = tr.find('td', attrs={'data-title': 'PORT'})
            if ip and port:
                proxy = ip.get_text() + ':' + port.get_text()
                proxy_list.append(proxy)
        return proxy_list


if __name__ == '__main__':
    ProxyCrawl().get_proxy()
