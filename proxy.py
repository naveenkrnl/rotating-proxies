import requests
from lxml.html import fromstring
import random


def get_proxy():
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = []
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.append(proxy)
    return proxies

def get_response(url):
    if 'https://' not in url:
        return "Incorrect url"
    while(True):
        proxies=get_proxy()
        proxy=random.choice(proxies)
        print(proxy)
        try:
            response = requests.get(url,proxies={"http": proxy, "https": proxy},headers={'User-Agent' : "Magic Browser"})
            print(proxy,"worked")
            return response
            break
        except:
            print("Retrying with diffrent Proxy")
    