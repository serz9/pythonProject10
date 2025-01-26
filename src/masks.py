from typing import Union

def get_mask_card_number(cartdate: Union[str]) -> Union[str]:

    """функция возвращает скрытый номер банковской карты"""

    cartdate_number = []
    cartdate_letter = []
    cartdate_ = cartdate.lower()

    for i in cartdate_:
        if i == ' ' or  i.isnumeric() == True:
            cartdate_number.append(i)
        if i == ' ' or i.isalpha() == True:
            cartdate_letter.append(i)

    cartdate_2 = ''.join(cartdate_number)
    cartdate_3 = ''.join(cartdate_letter)
    cartdate_4 = cartdate_3.strip()
    new_cartdate = cartdate_4 + " "+ cartdate_2.strip()
    print(new_cartdate)
    return new_cartdate

def get_mask_account(bankaccount: Union[str]) -> Union[str]:

    """функция возвращает  скрытый номер банковского счета"""

    bankaccount_2 = []
    bankaccount_ = bankaccount.lower()

    for i in bankaccount_:
        if i == ' ' or i.isnumeric() == True:
            bankaccount_2.append(i)

    bankaccount_3 = ''.join(bankaccount_2)
    bankaccount_4 = bankaccount_3.strip()
    new_bankaccount = 'Счет'+ " " + len(bankaccount_4[12:14]) * "*" + bankaccount_4[14:20]
    print(new_bankaccount)
    return new_bankaccount



get_mask_card_number('Visa Gdjfjf 8384 8885 5999 8899')
get_mask_account('Счет 293848484005005500')