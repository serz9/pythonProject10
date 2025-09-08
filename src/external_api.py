import os
import requests
from dotenv import load_dotenv
import logging


load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

#logging.basicConfig(filename ='external_api',
                   # level = logging.INFO,
                   # format = '%(asctime)s %(level)s :%(massege)s',
                   #filemode ='w')

#my_logger = logging.getLogger(__name__)
#my_logger.setLevel(logging.INFO)
#my_consol_handler = logging.StreamHandler()
#my_consol_formatter = logging.Formatter('%(asctime)s %(level name)s: %(message)s')
#my_logger.addHandler(my_consol_handler)
#my_file_handler = logging.FileHandler(filename='external_api.logs',mode = 'w',encoding='utf-8')
#my_logger.addHandler(my_file_handler)
#my_file_formatter = logging.Formatter('%(asctime)s %(level name)s: %(message)s')
#my_logger.addHandler(my_file_handler)
#my_file_handler.setFormatter(my_file_formatter)

#logging.debug('выполнение программы')
#logging.info('важная информация')
#logging.warning('внимание')
#logging.error('произошла ошибка')
#logging.critical('критический уровень опасности')
#my_logger =logging.getLogger(__name__)

#API_KEY = os.getenv('API_KEY')
#BASE_URL = os.getenv('BASE_URL')

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
    """
    Возвращает результат транзакции в рублях
    """
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency_code = transaction['operationAmount']['currency']['code']

        if currency_code == "RUB":
            print(amount)
            return amount

        rate = get_exchange_rate(currency_code)
        if rate is None:
            raise ValueError('Не удалось получить курс валют')

        rub_amount = amount * rate
        return round(rub_amount, 2)

    except Exception as e:
        logging.error(f'Непредвиденная ошибка: {e}')
        return None


def get_exchange_rate(currency) :


    try:
        headers = {'apikey': API_KEY}

        params = {
               'symbols': currency,
               'base' :'RUB'

        }
        response = requests.get(BASE_URL,params=params,headers=headers)
        response.raise_for_status()
        data = response.json()

        return data['rates']['currency']

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









