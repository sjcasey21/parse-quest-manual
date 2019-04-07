import bs4
from itertools import takewhile
from .utils import parse_row


def parse_table(table: bs4.element.Tag):
    head, *rows = table.find_all('tr')
    head = [i.text.strip() for i in head.find_all('td')]
    rows = [[i.text.strip() for i in row.find_all('td')] for row in rows]

    data = [parse_row(dict(zip(head, row))) for row in rows]
    return data


def chunk_categories(start_node):
    nodes = [start_node, *start_node.find_all_next('h3')]
    nodes = [{
        'category':
        node.text.strip().lower(),
        'content': [
            tag for tag in takewhile(
                lambda x: x.name > 'h3',
                node.find_next_siblings(True),
            )
        ],
    } for node in nodes]

    return nodes


def parse_contents(categories):
    return [{
        **category, 'content': [{
            'items': parse_table(tag)
        } for tag in category['content'] if tag.name == 'table']
    } for category in categories]
