import logging
from typing import Union

masks_logger = logging.getLogger("masks_logger")
masks_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/masks_logs.log", encoding="utf-8")
file_handler.encoding = "utf-8"

file_formatter = logging.Formatter(" %(asctime)s %(name)s %(levelname)s: %(message)s ")
file_handler.setFormatter(file_formatter)

masks_logger.addHandler(file_handler)


def get_mask_card_number(cartdate: Union[str]) -> Union[str]:

    """Функция возвращает скрытый номер банковской карты"""

    try:
        if cartdate.isdigit() == False:
            masks_logger.info(" Введены не корректные данные ")
            print(" Некорректные данные ")
            return " Некорректные данные "
        if len(cartdate) > 16:
            masks_logger.infio(" Ведено колличество символов более необходимого ")
            print(" Вы ввели количество символов более необходимого ")
            return " Вы ввели количество символов более необходимого "
        if len(cartdate) < 16:
            masks_logger.info(" Введено колличество символов менее необходимого ")
            print(" Вы ввели  менее необходимого количество символов ")
            return " Вы ввели количество символов менее необходимого "

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

        print(new_cartdate)
        masks_logger.info(" отработала функция  get_mask_card_number ")
        return new_cartdate
    except Exception as e:
        masks_logger.error(f"ошибка {str(e)}")


def get_mask_account(bankaccount: Union[str]) -> Union[str]:
    """Функция возвращает  скрытый номер банковского счета"""
    try:
        if bankaccount.isdigit() == False:
            print(" Некорректные данные ")
            masks_logger.info("Введены некоректные данные")
            return " Некорректные данные "
        if len(bankaccount) > 20:
            print(" Вы ввели количество символов более необходимого ")
            masks_logger.info("Введено колличество сиволов более необходимого")
            return " Вы ввели количество символов более необходимого "
        if len(bankaccount) < 20:
            print(" Вы ввели количество символов  менее необходимого")
            masks_logger.info("Введено колличество символов менее необходимого")
            return " Вы ввели количество символов менее необходимого "

        new_bankaccount = len(bankaccount[14:16]) * "*" + bankaccount[16:20]
        print(new_bankaccount)
        masks_logger.info("отроботала функция get_mask_account")
        return new_bankaccount
    except Exception as e:
        masks_logger.error(f"ошибка {str(e)}")


if __name__ == "__main__":  # pragma : no cover

    get_mask_card_number("3345555559998899")
    get_mask_account("83848885599988999879")
