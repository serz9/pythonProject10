import pytest
import pandas as pd
from unittest.mock import mock_open
from src.masks import get_mask_account, get_mask_card_number
from src.processing import sort_by_date
from src.widget import get_time, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions, tranzactions_list, card_number_generator
from src.decorators import functt
from src.get_csv_exel import read_csv_transactions, read_excel_transactions


def test_get_mask_card_number():

    """   Проверка на соответствие выходных параметров ожидаемым   """

    assert get_mask_card_number('8384888559998899') == '8384 88** **** 8899'


def test_get_mask_card_number_long():

    """   Проверка на соответствие выходных параметров ожидаемым при привышении длины строки   """

    assert get_mask_card_number('83848885599988991') == " Вы ввели количество символов более необходимого "


def test_get_mask_card_number_error():

    """ Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных """

    assert get_mask_card_number('assdasddsdssassd') == " Некорректные данные "


def test_get_mask_card_number_short():

    """    Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных    """

    assert get_mask_card_number('384848') == " Вы ввели количество символов менее необходимого "


def test_get_mask_account_short():

    """    Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных    """

    assert get_mask_account('373664') == " Вы ввели количество символов менее необходимого "


def test_get_mask_account_long():

    """    Проверка на соответствие выходных параметров ожидаеемым  при привышении длинны строки   """

    assert get_mask_account('293848484005005500354323434') == " Вы ввели количество символов более необходимого "


def test_get_mask_account_error():

    """   Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных   """

    assert get_mask_account('ahshdjsjajsjdjfj') == " Некорректные данные "


def test_sort_by_date(coll_1):

    """   Проверка  сортировки по дате   """

    assert sort_by_date(coll_1) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize('value,expected', [('Счет 23452345234523452345', 'Счет **2345',),
                            ('Visa 3456 4657 5767 7373', 'Visa 3456 46** **** 7373')])

def test_get_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_filter_by_currency():

    """   Тест фильтрации данных   """

    res_ = list(filter_by_currency(tranzactions_list, 'USD'))
    assert res_ == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]


def test_transaction_descriptions(test_tranzact_list):

    """   Тест описание транзакций   """

    res_ = list(transaction_descriptions(test_tranzact_list))
    assert res_ == ['Перевод организации', 'Перевод со счета на счет']


def test_card_namber_generator():

    """   Функция проверки генератора номеров карт   """

    res = list(card_number_generator(1, 5))
    expected = [
    '0000 0000 0000 0001',
    '0000 0000 0000 0002',
    '0000 0000 0000 0003',
    '0000 0000 0000 0004',
    '0000 0000 0000 0005']

    assert res == expected


def test_decor():

    """    Функция проверки декоратора   """

    with pytest.raises(NameError) as func_errors:
        functt(5, 3)
        assert func_errors.value == NameError


def test_decorators(capsys):

    """    Функция проверки вывода в консоль   """

    print('functt ok')
    captured = capsys.readouterr()
    assert captured.out == 'functt ok\n'


def test_get_time():

    """   Функкция проверки  получения даты  и времени   """

    assert get_time('2018-11-07T13:12:05.485858') == '07.11.2018'


def test_read_csv_transaction(mocker):

    """    Функция мокирования ридера    """

    data_csv = """id;name
1;Eji 
2;Irji"""

    mocker.patch('builtins.open', mock_open(read_data=data_csv), create=True)
    result = read_csv_transactions('test_file')

    assert len(result) == 2
    assert result[1] == {'id': '2', 'name': 'Irji'}


def test_read_excel_transactions(mocker):

    """   Функция мокирует ексель  ридер   """

    data_excel = pd.DataFrame({'cl1': ['v1', 'v2'],
                               'cl2': ['v3', 'v4']})

    mocker.patch('pandas.read_excel', return_value=(data_excel))
    result = read_excel_transactions('test_file')

    assert len(result) == 2
    assert result[1] == {'cl1': 'v2', 'cl2': 'v4'}
