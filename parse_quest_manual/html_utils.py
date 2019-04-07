import bs4
from itertools import takewhile
from .dict_utils import parse_row


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
    def conditional_dict(key, value, func):
        return {key: func(value)} if value else {}

    def tag_to_str(tag):
        return str.lower(str.strip(bs4.element.Tag.getText(tag)))

    def limited_tag_search(start_node, search_tag, limit):
        return next(
            (tag
             for tag in start_node.find_previous_siblings(True, limit=limit)
             if tag.name == search_tag), None)

    return [{
        **category, 'content': [{
            **conditional_dict(
                'type',
                limited_tag_search(tag, 'h4', 2),
                tag_to_str,
            ),
            **conditional_dict(
                'subtype',
                limited_tag_search(tag, 'h5', 1),
                tag_to_str,
            ),
            'items':
            parse_table(tag),
        } for tag in category['content'] if tag.name == 'table']
    } for category in categories]


def parse_categories(start_node):
    categories = chunk_categories(start_node)
    categories = parse_contents(categories)
    return categories
