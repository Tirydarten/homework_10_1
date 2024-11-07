from datetime import datetime


def filter_by_state(dict_for_search: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state ('по умолчанию'EXECUTED') и
    возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    new_dicts = []
    for i in range(len(dict_for_search)):
        if dict_for_search[i]["state"] == state:
            new_dicts.append(dict_for_search[i])
    if new_dicts:
        return new_dicts
    return []


def sort_by_date(new_dicts_sort: list, sort_reverse: bool = True) -> list | str:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — сортировка по убыванию, т. е. сначала самые последние операции)"""
    try:
        for i in range(len(new_dicts_sort)):
            datetime.strptime(new_dicts_sort[i]["date"], "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return "Неверный формат даты"

    sorted_date = sorted(new_dicts_sort, key=lambda new_dict: new_dict["date"], reverse=sort_reverse)
    return sorted_date
