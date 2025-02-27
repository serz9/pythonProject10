from typing import Union
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(riquisites: str) -> str:

    """ функция возвращае замаскированный счет или номер банковской карты"""


    riquisites_letter: list[str] = []
    riquisites_number: list[str] = []

    riquisites_ = riquisites.split(' ')

    for i in riquisites_:
        if i.isnumeric() == True:
            riquisites_number.append(i)
        if i.isalpha() == True:
            riquisites_letter.append(i)

    riquisites_letter_ = ' '.join(riquisites_letter)
    riquisites_number_ = ''.join(riquisites_number)

    if riquisites_[0] != 'Счет':
        res = riquisites_letter_ + " " + get_mask_card_number(riquisites_number_)
        return res
    if riquisites_[0] == 'Счет':
        res = riquisites_letter_ + " " + get_mask_account(riquisites_number_)
        return res




mask_account_card('Счет 23452345234523452345')



def get_time(timest: Union[str]) -> str:

    """ функция изменяет формат строки в обьекте Data """

    timestr_ = list(timest.split('T'))
    timestr_1 = list(timestr_[0].split('-'))
    timestr_1.reverse()
    timestr_2 = str('.'.join(timestr_1))
    print(timestr_2)
    return timestr_2


get_time('2018-11-07T13:12:05.485858')