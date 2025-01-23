from datetime import *
from typing import Union
from src.masks import get_mask_card_number,get_mask_account


def mask_account_card(cart_count_date: Union[str]):
    """ функция возвращает замаскированные счет или номер банковской карты """
    letter_1 = []
    number_1 = []
    for i in cart_count_date:
        if i == " " or i.isalpha() == True:
            letter_1.append(i)
        if i.isnumeric() == True:
            number_1.append(i)

    letter_1_1 = ''.join(letter_1)
    number_1_1 = ''.join(number_1)

    res_1 = letter_1_1 + " " + get_mask_card_number(number_1_1)
    print(res_1)
    return res_1



mask_account_card('Visa Platinum 7000792289606361')


def get_time(timest: Union[str]):
    """ функция изменяет формат строки в обьекте Data """
    timestr_ = list(timest.split('T'))
    timestr_1 = list(timestr_[0].split('-'))
    timestr_1.reverse()
    timestr_2 = str('.'.join(timestr_1))
    print(timestr_2)
    return timestr_2


get_time('2018-11-07T13:12:05.485858')

