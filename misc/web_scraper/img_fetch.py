#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import requests
import urllib.request
from bs4 import BeautifulSoup

def usage():
    return " ".join(["usage:", sys.argv[0], "<url>"])


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(usage())
    else:
        response = requests.get(sys.argv[1])
        soup = BeautifulSoup(response.text)        

        texts = soup.text.split('\n')
        image_urls = [t for t in texts if t.startswith('https://') and (t.endswith('.jpg') or t.endswith('.png'))]
        
        for i, url in enumerate(image_urls):
            print('[*] fetching: {}'.format(url))
            urllib.request.urlretrieve(url, str(i) + '.jpg')
