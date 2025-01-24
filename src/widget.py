#from src.masks import *
from src.masks import get_mask_account, get_mask_card_number
from typing import Union

#def mask_counter(cart_count_date: Union[str]) -> Union[str]:
    #""" функция возвращает замаскированные счет или номер банковской карты """

    #letter_ = []
    #number_ = []

    #for i in cart_count_date:
        #if i == " " or i.isalpha() == True:
           # letter_.append(i)
        #if i.isnumeric() == True:
           # number_.append(i)

    #letter_1 = ''.join(letter_)
    #number_1 = ''.join(number_)

    #res = str(letter_1) + " " + str(number_1)
    #print(res)
    #return res

#mask_counter('Visa Platinum 7000792289606361')
def mask_account_card(riquisites: str) -> str:

    startstring = riquisites.startswith('счет')

    if startstring == True:
        return get_mask_account(riquisites)
    else:
        return get_mask_card_number(riquisites)



mask_account_card('Visa PLatinum 7000792289606361')


def get_time(timest: Union[str]):
    """ функция изменяет формат строки в обьекте Data """

    timestr_ = list(timest.split('T'))
    timestr_1 = list(timestr_[0].split('-'))
    timestr_1.reverse()
    timestr_2 = str('.'.join(timestr_1))
    print(timestr_2)
    return timestr_2


get_time('2018-11-07T13:12:05.485858')
