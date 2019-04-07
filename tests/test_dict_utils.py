from parse_quest_manual import dict_utils

# from dict_utils import parse_row, str_to_int, map_key, map_value


def test_map_key():
    assert dict_utils.map_key('someKey') == 'somekey'


def test_str_to_int():
    assert dict_utils.str_to_int('20') == 20
    assert dict_utils.str_to_int('a20a') == 20
    assert dict_utils.str_to_int('aa') == 0
    assert dict_utils.str_to_int('') == 0
    assert dict_utils.str_to_int('-20') == -20
    assert dict_utils.str_to_int('——') == 0


def test_dice_to_list():
    assert dict_utils.dice_to_list('  4 -1d20   ') == ['4', '-1d20']
    assert dict_utils.dice_to_list('4 +1d4') == ['4', '+1d4']
    assert dict_utils.dice_to_list('——') == []
    assert dict_utils.dice_to_list('10 DMG') == ['10']


def test_parse_traits():
    test_trait = ''.join([
        'Spread toxic ooze in 10ft. AoE. Character take 1d4',
        ' rad-level when they enter the area and ',
        'it acts as rough terrain.',
    ])
    assert dict_utils.parse_traits(test_trait) == [
        'spread toxic ooze in 10ft',
        'aoe',
        'character take 1d4 rad-level when they enter the area and it acts as rough terrain',
    ]
    assert dict_utils.parse_traits('Deals slash damage, Finesse weapon') == [
        'deals slash damage',
        'finesse weapon',
    ]
    assert dict_utils.parse_traits('——') == []
    assert dict_utils.parse_traits(' ') == []


def test_parse_row() -> None:
    test_armor = {
        'Name': 'All-nighter nightwear',
        'DT': '0 DT',
        'Value': '2 caps',
        'Weight': '1 lbs.',
        'Traits': '+1 END, +1 CHA',
    }
    assert dict_utils.parse_row(test_armor) == {
        'name': 'all-nighter nightwear',
        'dt': 0,
        'value': 2,
        'weight': 1,
        'traits': ['+1 end', '+1 cha']
    }

    test_melee_weapon = {
        'DMG': '10 +1d8',
        'ACC': '-1',
        'STR': '12 STR',
        'DEF': '+1'
    }

    assert dict_utils.parse_row(test_melee_weapon) == {
        'dmg': ['10', '+1d8'],
        'acc': -1,
        'str': 12,
        'def': 1
    }

    test_ranged_weapon = {
        'MAG': '1 shots',
        'Ammo': 'Darts',
    }

    assert dict_utils.parse_row(test_ranged_weapon) == {
        'mag': 1,
        'ammo': 'darts',
    }

    test_accessories = {
        'Area': 'Full body',
        'Available Weapons': 'Two-handed weapons',
        'DMG': '10 DMG'
    }

    assert dict_utils.parse_row(test_accessories) == {
        'area': 'full body',
        'available weapons': 'two-handed weapons',
        'dmg': ['10']
    }

    test_ammunition = {
        'Small Mag': '1 cap',
        'Medium Mag': '4 caps',
        'Large Mag': '50 caps',
        'Weapon Type': 'Ballistic',
        'Value Modifier': '+2 caps',
        'Effect': 'Gain +1d4 on your attack roll'
    }

    assert dict_utils.parse_row(test_ammunition) == {
        'small mag': 1,
        'medium mag': 4,
        'large mag': 50,
        'weapon type': 'ballistic',
        'value modifier': 2,
        'effect': ['gain +1d4 on your attack roll']
    }

    test_medical = {
        'Duration': '4 rounds',
        'Addiction Save DC': 'DC 4',
        'HP': '+1d4 HP',
        'RAD': '+1 RAD'
    }

    assert dict_utils.parse_row(test_medical) == {
        'duration': 4,
        'addiction save dc': 4,
        'hp': ['+1d4'],
        'rad': 1
    }

    test_misc = {
        'Component In': '12x Scope, ACOG scope, Piece Bayonet, Slash bayonet'
    }

    assert dict_utils.parse_row(test_misc) == {
        'component in':
        ['12x scope', 'acog scope', 'piece bayonet', 'slash bayonet']
    }

    assert dict_utils.parse_row({'Component In': '——'}) == {'component in': []}
