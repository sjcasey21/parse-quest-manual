import re
from ._constants_items import *
from ._constants_global import NULL_VALUE
from typing import Union, Dict


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
        DT: lambda: str_to_int(value),
        VALUE: lambda: str_to_int(value),
        WEIGHT: lambda: str_to_int(value),
        ACCURACY: lambda: str_to_int(value),
        DEFENSE: lambda: str_to_int(value),
        MAGAZINE: lambda: str_to_int(value),
        SMAG: lambda: str_to_int(value),
        MMAG: lambda: str_to_int(value),
        LMAG: lambda: str_to_int(value),
        RADIATION: lambda: str_to_int(value),
        STRENGTH: lambda: str_to_int(value),
        TRAITS: lambda: parse_traits(value),
        DAMAGE: lambda: dice_to_list(value),
        EFFECT: lambda: parse_traits(value),
        VALUEMOD: lambda: str_to_int(value),
        DURATION: lambda: str_to_int(value),
        ADDICTIONSAVE: lambda: str_to_int(value),
        HP: lambda: dice_to_list(value),
        RADIATION: lambda: str_to_int(value),
        COMPONENTIN: lambda: parse_traits(value)
    }

    return switcher.get(key, value.lower)()


def parse_row(row: Dict[str, str]) -> Dict[str, Union[int, str]]:
    return {map_key(key): map_value(key, val) for key, val in row.items()}
