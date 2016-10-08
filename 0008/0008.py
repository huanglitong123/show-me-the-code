#!/usr/bin/env python
# coding: utf-8
'''
安装python goose：
git clone https://github.com/grangier/python-goose.git
cd python-goose
pip install -r requirements.txt
python setup.py install
'''
from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 要分析的网页url
url = 'http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html'


def extract(url):
    '''
    提取网页正文
    '''
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == '__main__':
    print extract(url)
