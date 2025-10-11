import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_api_response():
    return {
        "rates": {
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


#Фикстура для транзакции в рублях

@pytest.fixture
def rub_transaction():
    return {
        'operationAmount': {
            'amount': '100.50',
            'currency': {'code': 'RUB'}
        }}
