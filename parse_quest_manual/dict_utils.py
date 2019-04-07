import re
from . import _constants_items as c
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
    if key in [
            c.DT,
            c.VALUE,
            c.WEIGHT,
            c.ACCURACY,
            c.DEFENSE,
            c.MAGAZINE,
            c.SMAG,
            c.MMAG,
            c.LMAG,
            c.RADIATION,
            c.STRENGTH,
            c.VALUEMOD,
            c.DURATION,
            c.ADDICTIONSAVE,
    ]:
        return str_to_int(value)
    elif key in [c.TRAITS, c.COMPONENTIN, c.EFFECT]:
        return parse_traits(value)
    elif key in [c.DAMAGE, c.HP]:
        return dice_to_list(value)
    else:
        return value.lower()


def parse_row(row: Dict[str, str]) -> Dict[str, Union[int, str]]:
    return {map_key(key): map_value(key, val) for key, val in row.items()}
