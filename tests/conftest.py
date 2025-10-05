import pytest
from unittest.mock import patch, MagicMock
@pytest.fixture
def test_tranzact_list():
    return [{
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
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": 'RUB',
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]

@pytest.fixture
def mock_api_response():
    return {
        "rates" : {
            "amount": "75.5",
            "currency": {
            "code": "USD"
        }
      }
    }



@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    monkeypatch.setenv('API_KEY', 'test_api_key')
    monkeypatch.setenv('BASE_URL', 'https://test.api.com')

#
#Фикстура для транзакции в рублях
@pytest.fixture
def rub_transaction():
    return {
        'operationAmount': {
            'amount': '100.50',
            'currency': {'code': 'RUB'}
        }}




