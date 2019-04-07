# -*- coding: utf-8 -*-
"""Main module."""
# !/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import bs4
import re
# import json
# import itertools
# from typing import Union, Dict, List
# from .utils import parse_row

# def parse_item_table(table_node: bs4.element.Tag):
#     table_title: str = table_node.previous_sibling.text
#     items = []
#     rows: List[bs4.element.Tag] = table_node.find_all('tr')
#
#     keys = [i.text for i in rows[0]]
#     for row in rows[1:]:
#         cols = [ele.text.strip() for ele in row.find_all('td')]
#         row_dict = dict(zip(keys, cols))
#         items.append(parse_row(row_dict))
#
#     return {'type': table_title.lower(), 'items': items}
#
#
# def parse_item_category(start_node, end_node=None):
#     if end_node is None:
#         category_tables = start_node.findAllNext('table')
#     else:
#         category_tables = list(
#             itertools.takewhile(
#                 lambda tag: tag.text != end_node.text,
#                 start_node.findAllNext([end_node.name, 'table'])))
#     category_tables = [parse_item_table(table) for table in category_tables]
#     return {'category': start_node.text, 'types': category_tables}
#
#
# def safe_index(i, lst):
#     return lst[i] if i < len(lst) else None
#
#
# def parse_categories(category_nodes):
#     return [
#         parse_item_category(category_nodes[i], safe_index(
#             i + 1, category_nodes)) for i, _ in enumerate(category_nodes)
#     ]

if __name__ == '__main__':  # pragma: no cover

    with open('quest-manual.html', 'r') as f:
        soup: bs4.BeautifulSoup = BeautifulSoup(f.read(), 'html.parser')

    ch15 = soup.find_all(text=re.compile('Chapter 15'))[1].parent

    item_categories = [i for i in ch15.findAllNext('h3')]
    # parse_item_category(item_categories[0], item_categories[1])
    # items = parse_categories(item_categories)
    # from pprint import pprint

    print(type(item_categories[0].findNext('table')))

    # print(json.dumps(items, indent=2))
    # with open('items.json', 'w') as f:
    #     json.dump(items, f, indent=2)
