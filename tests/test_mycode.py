from src.generators import filter_by_currency, transaction_descriptions, tranzactions_list
from src.utils import jsn_date
from src.external_api import get_exchange_rate
from src.external_api import convert_transaction
import os
from unittest.mock import MagicMock,patch

def test_filter_by_currency():

    """  Тест фильтрации данных  """

    res_ = filter_by_currency(tranzactions_list,  'USD')
    assert list(res_) == [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]


def test_transaction_descriptions():

    """   Тест описание транзакций   """

    assert list(transaction_descriptions(tranzactions_list)) == ['Перевод организации', 'Перевод со счета на счет']


def test_empty_file():

    with open('empty.json', 'w') as f:
        f.write('[]')

    result = jsn_date('empty.json')
    assert result == []
    os.remove('empty.json')


def test_valid_list():

    with open('test_list.json', 'w') as f:
        f.write('[{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]')

    result = jsn_date('test_list.json')
    expected = [{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]
    assert result == expected
    os.remove('test_list.json')

def test_exchange_rate():
    mock_response = MagicMock()
    mock_response.json.return_value = {
                        'rates': {"RUB": 75.0}
                                           }
    with patch('requests.get', return_value=mock_response):
        rate = get_exchange_rate('USD')
        assert rate == 75.0

def test_convert_transaction(eur_transaction) :

    with patch('src.external_api.get_exchange_rate',return_value = 75.0):
        res = convert_transaction(eur_transaction)
        assert res == 7500


def test_filter_by_currency():

    """  Тест фильтрации данных  """

    res_ = list(filter_by_currency(tranzactions_list,'USD'))
    assert res_ == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]


def test_transaction_descriptions():

    """   Тест описание транзакций   """

    assert list(transaction_descriptions(tranzactions_list)) == ['Перевод организации', 'Перевод со счета на счет']