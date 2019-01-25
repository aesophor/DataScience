#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

def usage():
    return " ".join(["usage: ", sys.argv[0], "<keyword>"])


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(usage())
    else:
        site_search_url = "https://shopee.tw/search?keyword="
        keyword = sys.argv[1]

        browser = webdriver.PhantomJS()
        browser.get(site_search_url + keyword)
        html = browser.page_soruce
        soup = BeautifulSoup(html)

        for item in soup.select('.col-xs-2-4 shopee-search-item-result__item'):
            name = item.select('._1NoI8_ KQFWxC')[0].text
            price = item.select('.tyA3vN _3eZ5Vz _3RuPcU')[0].text
            print("{} {}".format(name, price))
