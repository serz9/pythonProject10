import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.processing import sort_by_date, filter_by_state
from src.widget import mask_account_card, get_time

def test_get_mask_card_number():

    """ Проверка на соответствие выходных параметров ожидаемым """

    assert get_mask_card_number('8384888559998899') == '8384 88** **** 8899'


def test_get_mask_card_number_long():

    """ Проверка на соответствие выходных параметров ожидаемым при привышении длины строки """

    assert get_mask_card_number('83848885599988991') == '8384 88** **** 8899'


def test_get_mask_card_number_error():

    """ Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных """

    assert get_mask_card_number('assdasddsdssassd') == '8384 88** **** 8899'


def test_get_mask_card_number_short():

    """ Проверка на не соответствие выходных параметров ожидемых при заведомо не правильных входных """

    assert get_mask_card_number('384848') == '8384 88** **** 8899'


def test_get_mask_account():

    """ Проверка на соответствие выходных параметров при заведомо неправильных входных  """

    assert get_mask_account('293848484005005500555') == '**5500'


def test_get_mask_account_long():

    """ Проверка на соответствие выходных параметров ожидаеемым  при привышении длинны строки"""

    assert get_mask_account('293848484005005500') == '**5500'


def test_get_mask_account_error():

    """ Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных """

    assert get_mask_account('ahshdjsjajsjdjfj') == '**5500'


def test_get_mask_account_empty():

    """ Проверка на не соответствие выходных параметров ожидаеемым  при заведомо неправильных  входных """

    assert get_mask_account(' ') == ' **5500 '


def test_filter_by_state(coll):

    """ Проверка на правильность фильтрации """

    assert filter_by_state(coll) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date(coll_1):

    """ Проверка  сортировки по дате """

    assert sort_by_date(coll_1) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize('value,expected', [('Счет 23452345234523452345', 'Счет **2345',),
                            ('Visa 3456 4657 5767 7373', 'Visa 3456 46** **** 7373'),])
def test_get_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_time():
    assert get_time('2018-11-07T13:12:05.485858') == '07.11.2018'
