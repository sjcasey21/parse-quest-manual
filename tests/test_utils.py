from parse_quest_manual import utils

# from utils import parse_row, str_to_int, map_key, map_value


def test_str_to_int():
    assert utils.str_to_int('20') == 20
    assert utils.str_to_int('a20a') == 20
    assert utils.str_to_int('aa') == 0
    assert utils.str_to_int('') == 0


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
