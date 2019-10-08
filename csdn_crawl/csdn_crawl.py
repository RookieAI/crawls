import ssl
import random
import time
import urllib.request
from bs4 import BeautifulSoup

import config as cfg
import proxy_crawl


class CsdnCrawl:
    def __init__(self, proxy_list):
        self.user_agents = cfg.USER_AGENTS
        self.url_list = cfg.URL_LISTS
        self.proxy_list = proxy_list
        self.context = ssl._create_unverified_context()

    def brush(self):
        user_agent = random.choice(self.user_agents)
        proxy = random.choice(self.proxy_list)
        referer = random.choice(self.url_list)
        headers = {
            "Host": "blog.csdn.net",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": user_agent,
            "Referer": referer,
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        httpproxy_handler = urllib.request.ProxyHandler({"http": proxy})
        opener = urllib.request.build_opener(httpproxy_handler)
        urllib.request.install_opener(opener)
        request = urllib.request.Request(referer, headers=headers)
        response = urllib.request.urlopen(request, context=self.context)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser', from_encoding="iso-8859-1")

        # 网页解析有问题，暂且搁置
        print(soup.find_all(attrs={'class': "read-count"}))
        # read_count = soup.find_all('span', attrs={'class': 'read-count'})[0]
        # read_count = read_count.get_text()

        print('>> brush information ...')
        # print('>> access to {}, using proxy {}, read_count {}'.format(referer, proxy, read_count))


if __name__ == '__main__':
    proxy_spider = proxy_crawl.ProxyCrawl(1)
    proxyes = proxy_spider.get_proxy()
    # print(proxyes)

    while True:
        csdn_spider = CsdnCrawl(proxyes)
        csdn_spider.brush()
        time.sleep(15)
