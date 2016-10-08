# coding=utf-8
from collections import Counter
import re

"""
0004, 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""


def count_word(file_name):
    with open(file_name) as f:
        words = re.findall("\w+", f.read().lower())
        return Counter(words).most_common()

print count_word('english.txt')
