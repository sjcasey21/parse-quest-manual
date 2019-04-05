from bs4 import BeautifulSoup
from parse_quest_manual import table_parser
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

    assert table_parser.parse_table(test_table) == [{
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
