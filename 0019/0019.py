#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import codecs
from lxml import etree


def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    c = []
    for i in range(table.nrows):
        c.append([int(j) for j in table.row_values(i)[0:]])
    return c


def save_xml(data):
    output = codecs.open('numbers.xml', 'w', 'utf-8')
    root = etree.Element('root')
    numbers_xml = etree.ElementTree(root)
    numbers = etree.SubElement(root, 'numbers')
    numbers.append(etree.Comment(u'数字信息\n'))
    numbers.text = str(data)
    output.write(etree.tounicode(numbers_xml.getroot()))
    output.close()

if __name__ == '__main__':
    file = 'numbers.xls'
    a = read_xls(file)
    save_xml(a)
