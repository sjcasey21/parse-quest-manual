import bs4
from .utils import parse_row


def parse_table(table: bs4.element.Tag):
    head, *rows = table.find_all('tr')
    head = [i.text.strip() for i in head.find_all('td')]
    rows = [[i.text.strip() for i in row.find_all('td')] for row in rows]

    data = [parse_row(dict(zip(head, row))) for row in rows]
    return data
