import pytest
from src.generators import filter_by_currency, transaction_descriptions, tranzactions_list, card_number_generator
from src.external_api import convert_transaction, get_exchange_rate
import os
from src.decorators import log, functt
from unittest.mock import patch
from requests.exceptions import HTTPError


def test_filter_by_currency():

    """  Тест фильтрации данных  """

    res_ = list(filter_by_currency(tranzactions_list,'USD'))
    assert res_ == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]


def test_transaction_descriptions():

    """   Тест описание транзакций   """

    assert list(transaction_descriptions(tranzactions_list)) == ['Перевод организации', 'Перевод со счета на счет']



#def get_number(number):

    #"""   Функция  преобразует номера карт в формат 3432 3432 4343 4564   """

    #card_number = str(number).zfill(16)
    #formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
    #print(formatted_card_number)
    #return formatted_card_number#


#@pytest.mark.parametrize('test,expected',[('1232323423422233','1232 3234 2342 2233'),('2223324334343344','2223 3243 3434 3344')])
#def test_get_number(test, expected):

    #"""   Перевод номера в формат 1234 2343 3432 1432   """

    #assert get_number(test) == expected



def test_card_namber_generator():

    """   Функция генератор номеров карт   """

    assert list(card_number_generator(1, 5)) == ['0000 0000 0000 0001','0000 0000 0000 0002','0000 0000 0000 0003', '0000 0000 0000 0004' ,'0000 0000 0000 0005']

def test_decor():

    """   Тестируем декоратор   """

    with pytest.raises(NameError) as func_errors:
        func(5,3)
        assert func_errors.value == NameError

def test_decorators(capsys):

     """  Тестируем декоратор   """

     print('functt ok')
     captured = capsys.readouterr()
     assert captured.out == 'functt ok\n'




#from decorators import log, functt  # Импортируй свой декоратор и тестируемую функцию

# Создаём временный файл для логов
#log_file = 'log.txt'


#log_file = tempfile.NamedTemporaryFile(delete=False).name



log_file = 'logs.txt'
@log(filename=log_file)
def functt(arg):
    return arg

@pytest.mark.parametrize("arg", [10])
def test_log_file(arg):

    functt(arg)


    with open(log_file, 'r', encoding='utf-8') as f:
        logs = f.read()
        assert "functt ok" in logs


    os.remove(log_file)


def test_convert_transaction_rub():
    transaction = {
        'operationAmount': {
            'amount': '100.50',
            'currency': {
                'code': 'RUB'
            }
        }
    }
    result = convert_transaction(transaction)
    assert result == 100.50


@patch('requests.get')
def test_convert_transaction_usd(mock_get, mock_api_response):
    mock_get.return_value.json.return_value = mock_api_response
    transaction = {
    "operationAmount": {
            "amount": "100.50",
            "currency": {
            "code": 'USD'
            }
        }
    }
    result = convert_transaction(transaction)
    assert result == pytest.approx(7537.5)

@patch('requests.get')

def test_get_exchange_rate_success(mock_get, mock_api_response):

    """   Тесты для полученя курса валют   """

    mock_get.return_value.json.return_value = mock_api_response
    rate = get_exchange_rate('USD')
    assert rate == 75.0

@patch('requests.get')
def test_get_exchange_rate_error(mock_get):
    mock_get.side_effect = HTTPError('API error')
    rate = get_exchange_rate('USD')
    assert rate is None

def test_env_variables():

    """"  Тест на загрузку переменных окружения   """

    assert os.getenv('API_KEY') is not None
    assert os.getenv('BASE_URL') is not None


def test_convert_transaction_invalid_data():

    """   Тест на правильность ввведенных  данных   """


    invalid_transaction = {
        'operationAmount': {
            'amount': 'abc',
            'currency': {
                'code': 'RUB'
            }
        }
    }

    result = convert_transaction(invalid_transaction)
    assert result is None

