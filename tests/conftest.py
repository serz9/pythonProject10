import pytest

<<<<<<< HEAD
#@pytest.fixture
#def coll():
    #return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]

#@pytest.fixture
##def coll():
    #return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
@pytest.fixture
def coll_1():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
=======

@pytest.fixture
def test_tranzact_list():
    return  [
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
         }]
>>>>>>> 7154f6990c20396387b67fbe9ad25824b57f898e
