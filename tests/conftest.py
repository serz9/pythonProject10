from unittest.mock import Mock

import pytest


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


@pytest.fixture
def rub_transaction():
    return {
        'operationAmount': {
            'amount': '100.50',
            'currency': {'code': 'RUB'}
        }}
@pytest.fixture
def eur_transaction():
    return {
        'operationAmount': {
            'amount': '100',
            'currency': {'code': 'EUR'}
        }}