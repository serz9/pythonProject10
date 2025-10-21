import pytest

from unittest.mock import Mock
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, tranzactions_list
from src.masks import get_mask_account, get_mask_card_number
from src.processing import sort_by_date
from src.widget import get_time, mask_account_card
from src.decorators import log


def test_get_mask_card_number():

    """   Проверка на соответствие выходных параметров ожидаемым   """

    assert get_mask_card_number("8384888559998899") == "8384 88** **** 8899"


def test_get_mask_card_number_long():

    """   Проверка на соответствие выходных параметров ожидаемым при привышении длины строки   """

    assert get_mask_card_number("83848885599988991") == " Вы ввели количество символов более необходимого "


def test_get_mask_card_number_error():

    """   Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных   """

    assert get_mask_card_number("assdasddsdssassd") == " Некорректные данные "


def test_get_mask_card_number_short():

    """   Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных   """

    assert get_mask_card_number("384848") == " Вы ввели количество символов менее необходимого "


def test_get_mask_account_short():

    """   Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных   """

    assert get_mask_account("373664") == " Вы ввели количество символов менее необходимого "


def test_get_mask_account_long():

    """   Проверка на соответствие выходных параметров ожидаеемым  при привышении длинны строки   """

    assert get_mask_account("293848484005005500354323434") == " Вы ввели количество символов более необходимого "


def test_get_mask_account_error():

    """   Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных   """

    assert get_mask_account("ahshdjsjajsjdjfj") == " Некорректные данные "



def test_sort_by_date(coll_1):

    """   Проверка  сортировки по дате   """

    assert sort_by_date(coll_1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "value,expected",
    [
        (
            "Счет 23452345234523452345",
            "Счет **2345",
        ),
        ("Visa 3456 4657 5767 7373", "Visa 3456 46** **** 7373"),
    ],
)
def test_get_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_filter_by_currency():

    """   Тест фильтрации данных   """

    res_ = list(filter_by_currency(tranzactions_list, "USD"))
    assert res_ == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


def test_transaction_descriptions(test_tranzact_list):

    """   Тест описание транзакций   """

    result = list(transaction_descriptions(test_tranzact_list))
    print(result)
    assert result == ["Перевод организации", "Перевод со счета на счет"]


def test_card_namber_generator():

    """   Функция проверки генератора номеров карт   """

    res = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    assert res == expected


def test_decorator_with_mock():
    mock_func = Mock(return_value="mocked")
    dec_func = log(mock_func)

    result = dec_func(5)

    mock_func.assert_called_once_with(5)
    assert result == "mocked"


def test_decor():
    with pytest.raises(NameError) as func_errors:
        functt("5")
        assert func_errors.value == NameError


def test_decorators(capsys):
    print("functt ok")
    captured = capsys.readouterr()
    assert captured.out == "functt ok\n"


def test_get_time():
    assert get_time("2018-11-07T13:12:05.485858") == "07.11.2018"
