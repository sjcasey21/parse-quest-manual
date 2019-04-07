from bs4 import BeautifulSoup
import bs4
from parse_quest_manual import html_utils
from pprint import pprint


def test_parse_table():
    source = '''
    <table>
        <tbody>
          <tr>
            <td>
              <p><strong>Name</strong></p>
            </td>
            <td>
              <p><strong>DT</strong></p>
            </td>
            <td>
              <p><strong>Value</strong></p>
            </td>
            <td>
              <p><strong>Weight</strong></p>
            </td>
            <td>
              <p><strong>Traits</strong></p>
            </td>
          </tr>
          <tr>
            <td>
              <p>Advanced radiation suit</p>
            </td>
            <td>
              <p>2 DT</p>
            </td>
            <td>
              <p>12 caps</p>
            </td>
            <td>
              <p>7 lbs.</p>
            </td>
            <td>
              <p>+4 rad res., <em>Bodysuit</em></p>
            </td>
          </tr>
        </tbody>
    </table>
    '''
    soup = BeautifulSoup(source.strip(), 'html.parser')
    test_table = soup.find('table')

    assert html_utils.parse_table(test_table) == [{
        'name':
        'advanced radiation suit',
        'dt':
        2,
        'value':
        12,
        'weight':
        7,
        'traits': ['+4 rad res', 'bodysuit']
    }]


def test_chunk_categories():
    source = '''
    <h2>something</h2>
    <p>some stuff before the items</p>
    <h3>Armor Sets</h3>
    <table></table>
    <h3>Helmets</h3>
    <p>some descriptions</p>
    <h4>some sub types</h4>
    <h1>a different section</h1>
    '''
    soup = BeautifulSoup(source.strip(), 'html.parser')
    test_document = soup.find('h3')

    result = html_utils.chunk_categories(test_document)
    assert [category['category']
            for category in result] == ['armor sets', 'helmets']
    assert [len(category['content']) for category in result] == [1, 2]


def test_parse_contents():
    armor = '''
    <table>
        <tbody>
          <tr>
            <td><p><strong>Name</strong></p></td>
            <td><p><strong>DT</strong></p></td>
            <td><p><strong>Value</strong></p></td>
            <td><p><strong>Weight</strong></p></td>
            <td><p><strong>Traits</strong></p></td>
          </tr>
          <tr>
            <td><p>Advanced radiation suit</p></td>
            <td><p>2 DT</p></td>
            <td><p>12 caps</p></td>
            <td><p>7 lbs.</p></td>
            <td><p>+4 rad res., <em>Bodysuit</em></p></td>
          </tr>
        </tbody>
    </table>'''
    helmets = '''
    <table>
        <tbody>
          <tr>
            <td><p><strong>Name</strong></p></td>
            <td><p><strong>DT</strong></p></td>
            <td><p><strong>Value</strong></p></td>
            <td><p><strong>Weight</strong></p></td>
            <td><p><strong>Traits</strong></p></td>
          </tr>
          <tr>
            <td><p>Baseball cap</p></td>
            <td><p>0 DT</p></td>
            <td><p>1 caps</p></td>
            <td><p>1 lbs.</p></td>
            <td><p>+1 Melee weapons</p></td>
          </tr>
        </tbody>
    </table>'''
    source = '''
    <h2>something</h2>
    <p>some stuff before the items</p>
    <h3>Armor Sets</h3>
    {}
    <h3>Helmets</h3>
    <h4>Hats</h4>
    {}
    <p>some descriptions</p>
    <h4>some sub types</h4>
    <h1>a different section</h1>'''.format(armor, helmets)
    soup = BeautifulSoup(source, 'html.parser')
    categories = html_utils.chunk_categories(soup.find("h3"))
    categories = html_utils.parse_contents(categories)

    assert categories == [
        {
            'category':
            'armor sets',
            'content': [{
                'items': [{
                    'name': 'advanced radiation suit',
                    'dt': 2,
                    'value': 12,
                    'weight': 7,
                    'traits': ['+4 rad res', 'bodysuit']
                }]
            }]
        },
        {
            'category':
            'helmets',
            'content': [{
                'type':
                'hats',
                'items': [{
                    'name': 'baseball cap',
                    'dt': 0,
                    'value': 1,
                    'weight': 1,
                    'traits': ['+1 melee weapons']
                }]
            }]
        },
    ]
