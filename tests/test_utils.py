from parse_quest_manual import utils

# from utils import parse_row, str_to_int, map_key, map_value


def test_map_key():
    assert utils.map_key('someKey') == 'somekey'


def test_str_to_int():
    assert utils.str_to_int('20') == 20
    assert utils.str_to_int('a20a') == 20
    assert utils.str_to_int('aa') == 0
    assert utils.str_to_int('') == 0


def test_dice_to_list():
    assert utils.dice_to_list('  4 -1d20   ') == ['4', '-1d20']
    assert utils.dice_to_list('4 +1d4') == ['4', '+1d4']
    assert utils.dice_to_list('——') == []


def test_parse_traits():
    test_trait = ''.join([
        'Spread toxic ooze in 10ft. AoE. Character take 1d4',
        ' rad-level when they enter the area and ',
        'it acts as rough terrain.',
    ])
    assert utils.parse_traits(test_trait) == [
        'spread toxic ooze in 10ft',
        'aoe',
        'character take 1d4 rad-level when they enter the area and it acts as rough terrain',
    ]
    assert utils.parse_traits('Deals slash damage, Finesse weapon') == [
        'deals slash damage',
        'finesse weapon',
    ]
    assert utils.parse_traits('——') == []
    assert utils.parse_traits(' ') == []


def test_parse_row() -> None:
    test = {
        "name": "deathclaw gauntlet",
        "dmg": "4 +1d4",
        "acc": "+0",
        "str": "6 str",
        "value": "15",
        "weight": "5",
        "traits": "ignores dt"
    }
    assert utils.parse_row(test) == {
        'name': 'deathclaw gauntlet',
        'dmg': '4 +1d4',
        'acc': 0,
        'str': 6,
        'value': 15,
        'weight': 5,
        'traits': 'ignores dt'
    }
