# -*- coding: utf-8 -*-

import requests
import lxml.html

page = requests.get('http://tieba.baidu.com/p/2166231880').text
doc = lxml.html.document_fromstring(page)
for idx, el in enumerate(doc.cssselect('img.BDE_Image')):
    print idx, el
    with open('%03d.jpg' % idx, 'wb') as f:
        f.write(requests.get(el.attrib['src']).content)
