import pytest
from generators.generators import filter_by_carrency,transaction_descriptions,tranzactions_list

def test_filter_by_carrency(filter_by_carrency):

    """  тест фильтрации данных  """

    res_ = list(filter_by_carrency(tranzactions_list))
    print(res)
    expected == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]
    assert res_ == expected




def test_transaction_descriptions(transaction_descriptions):

    res_ = transactions_discription(tranzact_list)
    assert res_ == ['Перевод организации', 'Перевод со счета на счет']

