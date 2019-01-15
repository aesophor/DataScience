#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    resp = requests.get("https://shopee.tw/search?keyword=macbook")
    print(resp.text)
