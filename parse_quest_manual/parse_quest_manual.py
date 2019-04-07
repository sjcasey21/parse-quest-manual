# -*- coding: utf-8 -*-
"""Main module."""
# !/usr/bin/env python
# coding: utf-8

import re
import bs4
from bs4 import BeautifulSoup
from .html_utils import parse_categories


def parse_manual(source):
    soup = BeautifulSoup(source, 'html.parser')
    start_node = soup.find(string=re.compile('Chapter 15')).find_parent('h2')
    return parse_categories(start_node)


if __name__ == '__main__':  # pragma: no cover

    with open('quest-manual.html', 'r') as f:
        soup: bs4.BeautifulSoup = BeautifulSoup(f.read(), 'html.parser')

    # ch15 = soup.find_all(text=re.compile('Chapter 15'))[1].parent
    ch15 = soup.find(string=re.compile('Chapter 15')).find_parent('h2')
    print(ch15)

    # item_categories = [i for i in ch15.findAllNext('h3')]
    # parse_item_category(item_categories[0], item_categories[1])
    # items = parse_categories(item_categories)
    # from pprint import pprint

    # print(type(item_categories[0].findNext('table')))

    # print(json.dumps(items, indent=2))
    # with open('items.json', 'w') as f:
    #     json.dump(items, f, indent=2)
