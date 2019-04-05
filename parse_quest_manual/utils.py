import re
from parse_quest_manual import _constants_items as c
from typing import Union, Dict

NULL_VALUE = '——'


def map_key(key: str) -> str:
    return key.lower()


def str_to_int(value: str) -> int:
    digits = ''.join(c for c in value if c.isdigit() or c == '-')
    return int(digits) if len(digits) else 0


def dice_to_list(dice):
    values = re.findall(r'[-+]?\d+d\d+|\d+', dice)
    return values if dice.strip() != NULL_VALUE else []


def parse_traits(traits):
    traits = traits.strip()
    if traits in [NULL_VALUE, '']:
        return []

    trait_list = re.split(r',|\.', traits)
    return [trait.strip().lower() for trait in trait_list if len(trait)]


def map_value(key: str, value: str) -> Union[int, str]:
    key = key.lower()
    switcher = {
        c.DT: lambda: str_to_int(value),
        c.VALUE: lambda: str_to_int(value),
        c.WEIGHT: lambda: str_to_int(value),
        c.ACCURACY: lambda: str_to_int(value),
        c.DEFENSE: lambda: str_to_int(value),
        c.MAGAZINE: lambda: str_to_int(value),
        c.SMAG: lambda: str_to_int(value),
        c.MMAG: lambda: str_to_int(value),
        c.LMAG: lambda: str_to_int(value),
        c.RADIATION: lambda: str_to_int(value),
        c.STRENGTH: lambda: str_to_int(value),
        c.TRAITS: lambda: parse_traits(value),
        c.DAMAGE: lambda: dice_to_list(value),
        c.EFFECT: lambda: parse_traits(value),
        c.VALUEMOD: lambda: str_to_int(value),
        c.DURATION: lambda: str_to_int(value),
        c.ADDICTIONSAVE: lambda: str_to_int(value),
        c.HP: lambda: dice_to_list(value),
        c.RADIATION: lambda: str_to_int(value),
        c.COMPONENTIN: lambda: parse_traits(value)
    }

    return switcher.get(key, value.lower)()


def parse_row(row: Dict[str, str]) -> Dict[str, Union[int, str]]:
    return {map_key(key): map_value(key, val) for key, val in row.items()}
