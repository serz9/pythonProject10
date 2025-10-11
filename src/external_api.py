import os
import requests
from dotenv import load_dotenv
import logging
import logging.config


load_dotenv()



API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY не найден в переменых окружения")


logging.basicConfig(

    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[



        logging.FileHandler('../logs/external_api.log'),
        logging.StreamHandler()
    ],
    encoding='utf-8'
)

my_logger = logging.getLogger(__name__)

def convert_transaction(transaction):

    """   Возвращает результат транзакции в рублях   """

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
        logging.error(f'Непредвиденная ошибка:{e}')
    return None


def get_exchange_rate(currency):

    try:
        headers = {'apikey': API_KEY}

        params = {
               'symbols': 'RUB',
               'base': currency

        }
        response = requests.get('https://api.apilayer.com/exchangerates_data/latest', params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'rates' in data and 'RUB' in data['rates']:
            return data['rates']['RUB']
        else:
            raise ValueError("Неверный формат ответа от API")


    except Exception as e:
        my_logger.error(f'ошибка {str(e)}')


if __name__ =='__main__':

    convert_transaction( {
        'operationAmount': {
            'amount': '100.50',
            'currency': {
                'code': 'USD'
            }
        }
    })







