import pytest
from src.generators import filter_by_currency, transaction_descriptions, tranzactions_list, card_number_generator



def test_filter_by_currency():

        """  Тест фильтрации данных  """


        res_ = filter_by_currency(tranzactions_list,'USD')
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

