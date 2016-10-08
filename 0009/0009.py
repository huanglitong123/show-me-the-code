# coding=utf-8
import requests as req
from bs4 import BeautifulSoup
"""
0009:一个HTML文件，找出里面的链接。
"""


def show_href(url):
    content = req.get(url).content
    soup = BeautifulSoup(content, "lxml")
    for tag in soup.find_all('a'):
        if tag.get('href').startswith('http'):
            print tag.get('href')


if __name__ == '__main__':
    show_href('http://www.mzitu.com/all/')
