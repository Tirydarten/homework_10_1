from typing import Any


def get_mask_card_number(number: Any) -> str:
    """Функция принимает строку и возвращает маски карты"""
    for arg in [number]:
        if not isinstance(arg, str):
            return "Ошибка типа данных"
    try:
        if (number[-16:].isdigit() and len(number) >= 21 and len(number.split()[-1]) == 16) is True:
            new_string_card = f"** **** {number[-4:]}"
        return new_string_card

    except UnboundLocalError:
        return "Неверный формат номера карты"


def get_mask_account(number: Any) -> str:
    """Функция принимает строку и возвращает маски счёта"""
    for arg in [number]:
        if not isinstance(arg, str):
            return "Ошибка типа данных"
    if (
        number[-20:-1].isdigit() and len(number) == 25 and number[:-21].isalpha() and len(number.split()[-1]) == 20
    ) is True:
        new_string_account = f"**{number[-4:]}"
        return new_string_account
    else:
        return "Ошибка в номере счета карты"
