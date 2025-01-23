from typing import Union


def get_mask_card_number(cartdate: Union[str]) -> Union[str]:
    """функция возвращает скрытый номер банковской карты"""
    new_cartdate = (
        cartdate[0:4]
        + " "
        + cartdate[4:6]
        + len(cartdate[6:8]) * "*"
        + " "
        + len(cartdate[8:12]) * "*"
        + " "
        + cartdate[12:16]
    )

    return new_cartdate


def get_mask_account(bankaccount: Union[str]) -> Union[str]:
    """функция возвращает  скрытый номер банковского счета"""
    new_bankaccount = len(bankaccount[14:16]) * "*" + bankaccount[16:20]
    return new_bankaccount


