import os
import requests
from dotenv import load_dotenv
import logging

a = os.getcwd()
print(a)
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('../logs/external_api.logs'),
        logging.StreamHandler()
    ],
    encoding='utf-8'
)

my_logger = logging.getLogger(__name__)

def convert_transaction(transaction):

    """
    Возвращает результат транзакции в рублях

    """
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency_code = transaction['operationAmount']['currency']['code']

        if currency_code == "RUB":
            return amount
        else:
            rate = get_exchange_rate(currency_code)

        if rate is None:
            raise ValueError('Не удалось получить курс валют')
        rub_amount = amount*rate

        return round(rub_amount, 2)

    except Exception as e:
        logging.error(f'Непредвиденная ошибка: {e}')
        return None


def get_exchange_rate(currency) :


    try:
        headers = {'apikey': API_KEY}

        params = {
               'symbols':'RUB',
               'base' :'currency'

        }
        response = requests.get('https://apilayer.com/marketplace/exchangerates_data/latest',params=params,headers=headers)
        response.raise_for_status()
        data = response.json()

        return data['rates']['RUB']

    except Exception as e:
        my_logger.error(f'ошибка {str(e)}')



convert_transaction( {
        'operationAmount': {
            'amount': '100.50',
            'currency': {
                'code': 'RUB'
            }
        }
    })









