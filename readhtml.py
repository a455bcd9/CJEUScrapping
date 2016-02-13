#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import html, etree
import requests

url = "http://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:62012TJ0562"

page = requests.get(url)
tree = html.fromstring(page.content.decode("utf8"))

content = tree.xpath('/html/body/*')

# print(etree.tostring(content, pretty_print=True))

# print content

# for string in content:
#   print(etree.tostring(string, method='html', encoding="UTF-8", pretty_print=True))

fulltext = ''

for string in content:
    fulltext += etree.tostring(string, method='html', encoding="UTF-8", pretty_print=True)

# print fulltext
print fulltext

# fileToWrite = 'test.html'

# with open(fileToWrite, 'w') as outfile:
#     for string in content:
#         outfile.write(etree.tostring(string, method='html', encoding="UTF-8", pretty_print=True))