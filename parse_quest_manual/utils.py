from typing import Union, Dict


# dice regex: (\+|\-)?(\d+d\d+)|\d+
def map_key(key: str) -> str:
    return key.lower()


def str_to_int(value: str) -> int:
    digits = ''.join(c for c in value if c.isdigit())
    return int(digits) if len(digits) else 0


# def str_to_dice_list(value):
#     #     return value
#     return re.compile(r'\b[+-]?(\d+d\d+)|\b\d+$').findall(value)


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
        # 'dmg': lambda: str_to_dice_list(value)
    }

    return switcher.get(key, value.lower)()


def parse_row(row: Dict[str, str]) -> Dict[str, Union[int, str]]:
    return {map_key(key): map_value(key, val) for key, val in row.items()}
