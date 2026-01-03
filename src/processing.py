from datetime import datetime
from typing import Any


def filter_by_state(dictioneris: list[dict[str, Any]], state: str = None) -> list[dict[str, Any]]:

    """   Функция сортировки словаря    """

    dictioneris_1: list = []

    for i in dictioneris:
        if i['state'] == state:
            dictioneris_1.append(i)

    print(dictioneris_1)
    return dictioneris_1


filter_by_state([{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'EXECUTED')


def sort_by_date(dictionaries: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:

    """   функция сортировки по дате по убыванию   """

    return sorted(dictionaries, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse)


sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],)
