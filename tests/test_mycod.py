import pytest
from generatorss.generators import filter_by_carrency, transaction_descriptions,get_number ,tranzactions_list, card_number_generator,number

def test_filter_by_carency():

    """  тест фильтрации данных  """

    res_ = list(filter_by_carrency(tranzactions_list,'USD'))
    assert res_ == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]


def test_transaction_descriptions(transaction_descriptions):

    """   Тест описание транзакций   """

    res_ == list(transaction_discriptions(tranzactions_list))
    assert res_ == ['Перевод организации', 'Перевод со счета на счет']


@pytest.mark.parametrize('test,expected',[('1232323423422233','1232 3234 2342 2233'),('2223324334343344','2223 3243 3434 3344')])
def test_get_number(test, expected):

    """   Перевод номера в формат XXXX XXXX XXXX 1432   """

    assert get_number(test) == expected


def test_card_number_generator(card_number_generator):

    """   Функция генератор номеров карт   """

    res = (card_number_generator(1, 1))
    assert res == '0000 0000 0000 0001'










