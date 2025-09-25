import pytest
from unittest.mock import patch, Mock
@pytest.fixture
def test_tranzact_list():


    {
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
                     "name": 'USD',
                     "code": "USD"
                 }

           },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
         }



@pytest.fixture
def arg():
    return 10



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



# Пример фикстуры с тестовым ответом API
@pytest.fixture
def mock_api_response():
    return {
        "rates": {
            "USD": 75.0,  # Курс USD к локальной валюте
            "EUR": 85.0
        },
        "base": "USD",
        "date": "2023-10-01"
    }


@patch('requests.get')  # Патчим requests.get
def test_convert_transaction_usd(mock_get, mock_api_response):
    # Создаем мок-ответ для requests.get
    mock_response = Mock()
    mock_response.status_code = 200  # Устанавливаем статус ответа
    mock_response.json.return_value = mock_api_response  # Задаем JSON-ответ

    # Настраиваем мок так, чтобы при вызове requests.get возвращался наш мок-ответ
    mock_get.return_value = mock_response

    # Создаем тестовую транзакцию
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {
                "code": 'USD'
            }
        }
    }

    # Вызываем тестируемую функцию
    result = convert_transaction(transaction)

    # Проверяем результат конвертации
    assert result == pytest.approx(7537.5)  # 100.50 * 75.0 = 7537.5

    mock_get.assert_called_once()  # Проверяем, что метод вызывался один раз

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
        }
    }




# Фикстура для мока ответа API
@pytest.fixture
def mock_api_response():
    return {
        'rates': {'RUB': 75.0},
        'success': True
    }


# Фикстура для настройки переменных окружения
@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    monkeypatch.setenv('API_KEY', 'test_api_key')
    monkeypatch.setenv('BASE_URL', 'https://test.api.com')


# Фикстура для транзакции в рублях
@pytest.fixture
def rub_transaction():
    return {
        'operationAmount': {
            'amount': '100.50',
            'currency': {'code': 'RUB'}
        }
    }


# Фикстура для транзакции в долларах
@pytest.fixture
def usd_transaction():
    return {
        'operationAmount': {
            'amount': '100.50',
            'currency': {'code': 'USD'}
        }
    }


# Фикстура для мока requests.get
@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'rates': {'RUB': 75.0},
            'success': True
        }
        mock_response.status_code = 200
        mock.return_value = mock_response
        yield mock


# Фикстура для некорректной транзакции
@pytest.fixture
def invalid_transaction():
    return {
        'operationAmount': {
            'amount': 'abc',
            'currency': {'code': 'RUB'}
        }
    }


# Фикстура для ошибки HTTP
@pytest.fixture
def http_error():
    return HTTPError('API error')