import pytest
<<<<<<< HEAD
from src.masks import get_mask_account, get_mask_card_number
from src.processing import sort_by_date
from src.widget import get_time, mask_account_card


def test_get_mask_card_number():

    """ Проверка на соответствие выходных параметров ожидаемым """

    assert get_mask_card_number('8384888559998899') == '8384 88** **** 8899'


def test_get_mask_card_number_long():

    """ Проверка на соответствие выходных параметров ожидаемым при привышении длины строки """

    assert get_mask_card_number('83848885599988991') == " Вы ввели количество символов более необходимого "


def test_get_mask_card_number_error():

    """ Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных """

    assert get_mask_card_number('assdasddsdssassd') == " Некорректные данные "


def test_get_mask_card_number_short():

    """ Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных """

    assert get_mask_card_number('384848') == " Вы ввели количество символов менее необходимого "


def test_get_mask_account_short():

    """ Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных """

    assert get_mask_account('373664') == " Вы ввели количество символов менее необходимого "


def test_get_mask_account_long():

    """ Проверка на соответствие выходных параметров ожидаеемым  при привышении длинны строки"""

    assert get_mask_account('293848484005005500354323434') == " Вы ввели количество символов более необходимого "


def test_get_mask_account_error():

    """ Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных """

    assert get_mask_account('ahshdjsjajsjdjfj') == " Некорректные данные "


#def test_filter_by_state():

   # """ Проверка на правильность фильтрации """

   #assert filter_by_state([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           # {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date(coll_1):

    """ Проверка  сортировки по дате """

    assert sort_by_date(coll_1) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize('value,expected', [('Счет 23452345234523452345', 'Счет **2345',),
                            ('Visa 3456 4657 5767 7373', 'Visa 3456 46** **** 7373'),])
def test_get_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_time():
    assert get_time('2018-11-07T13:12:05.485858') == '07.11.2018'
=======
from src.generators import filter_by_currency, transaction_descriptions, tranzactions_list, get_number_generator

def test_filter_by_currency():

    """  Тест фильтрации данных  """

    res_ = list(filter_by_currency(tranzactions_list,'USD'))
    assert res_ == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]


def test_transaction_descriptions(test_tranzact_list):

    """   Тест описание транзакций   """

    res_ == list(transaction_descriptions(test_tranzact_list))
    assert res_ == ['Перевод организации', 'Перевод со счета на счет']



#def get_number(number):

    #"""   Функция  преобразует номера карт в формат 3432 3432 4343 4564   """

    #card_number = str(number).zfill(16)
    #formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
    #print(formatted_card_number)
    #return formatted_card_number#


#@pytest.mark.parametrize('test,expected',[('1232323423422233','1232 3234 2342 2233'),('2223324334343344','2223 3243 3434 3344')])
#def test_get_number(test, expected):

   # """   Перевод номера в формат 1234 2343 3432 1432   """

   # assert get_number(test) == expected


def test_card_namber_generator():

    """   Функция проверки генератора номеров карт   """

    res = list(get_number_generator(1,5))
    expected = [
'0000 0000 0000 0001',
'0000 0000 0000 0002',
'0000 0000 0000 0003',
'0000 0000 0000 0004',
'0000 0000 0000 0005']

    assert res == expected










>>>>>>> 7154f6990c20396387b67fbe9ad25824b57f898e
