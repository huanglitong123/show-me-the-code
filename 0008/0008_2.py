#!/usr/local/bin/python
# coding=utf-8
__author__ = 'Dineshkarthik'

# 0008 Title: an HTML file, find the inside of the body .


import requests
from bs4 import BeautifulSoup

url = "http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html"
page = requests.get(url).content
soup = BeautifulSoup(page, "lxml")

with open('result.txt', 'w') as f:
    f.write(soup.body.text.encode('utf-8'))
