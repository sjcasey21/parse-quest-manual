import re
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
        'dt': lambda: str_to_int(value),
        'value': lambda: str_to_int(value),
        'weight': lambda: str_to_int(value),
        'acc': lambda: str_to_int(value),
        'def': lambda: str_to_int(value),
        'mag': lambda: str_to_int(value),
        'small mag': lambda: str_to_int(value),
        'medium mag': lambda: str_to_int(value),
        'large mag': lambda: str_to_int(value),
        'rad': lambda: str_to_int(value),
        'str': lambda: str_to_int(value),
        'traits': lambda: parse_traits(value),
        'dmg': lambda: dice_to_list(value),
        'effect': lambda: parse_traits(value),
        'value modifier': lambda: str_to_int(value),
        'duration': lambda: str_to_int(value),
        'addiction save dc': lambda: str_to_int(value),
        'hp': lambda: dice_to_list(value),
        'rad': lambda: str_to_int(value),
        'component in': lambda: parse_traits(value)
    }

    return switcher.get(key, value.lower)()


def parse_row(row: Dict[str, str]) -> Dict[str, Union[int, str]]:
    return {map_key(key): map_value(key, val) for key, val in row.items()}
