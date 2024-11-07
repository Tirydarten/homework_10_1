from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция получает строку и маскирует счет/карту"""

    if (
        number[-20:-1].isdigit()
        and len(number) == 25
        and number[:-21].isalpha()
        and number[:-21] in "Счет"
        and len(number.split()[-1]) == 20
    ) is True:
        new_number_account = get_mask_account(number)
        result_account = f"{number[:-20]}{new_number_account}"
        return result_account

    elif (number[-16:].isdigit() and len(number) >= 21 and len(number.split()[-1]) == 16) is True:
        new_number_card = get_mask_card_number(number)
        result_card = f"{number[:-16]}{number[-16:-12]} {number[-12:-10]} {new_number_card}"
        return result_card
    else:
        return "Ошибка данных"


def get_date(user_date: str) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ"""

    if len(user_date) != 26:
        return "Ошибка типа данных"
    try:
        date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return "Неверный формат входящей даты"
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
