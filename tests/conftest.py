import pytest


@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "test_api_key")
    monkeypatch.setenv("BASE_URL", "https://test.api.com")


@pytest.fixture
def eur_transaction():
    return {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}
