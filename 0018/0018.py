#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import codecs
from lxml import etree
from collections import OrderedDict


def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    c = OrderedDict()
    for i in range(table.nrows):
        c[int(table.cell(i, 0).value)] = table.row_values(i)[1:]
    return c


def save_xml(data):
    output = codecs.open('city.xml', 'w', 'utf-8')
    root = etree.Element('root')
    city_xml = etree.ElementTree(root)
    city = etree.SubElement(root, 'city')
    city.append(etree.Comment(u'城市信息\n'))
    city.text = str(data)
    output.write(etree.tounicode(city_xml.getroot()))
    output.close()

if __name__ == '__main__':
    file = 'city.xls'
    a = read_xls(file)
    save_xml(a)
