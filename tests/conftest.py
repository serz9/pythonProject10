import pytest
from generators.generators import tranzactions_list


def filter_by_carrency(tranzactions_list: list[str], currency: [str]):

    """   функция фильтрации   """

    res = (i for i in tranzactions_list if i['operationAmount']['currency']['code'] == currency)
    for n in res:
        yield n


filter_run = filter_by_carrency(tranzactions_list, 'USD')
for tranzaction in filter_run:
    print(tranzaction)

filter_by_carrency(tranzactions_list, 'USD')
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
        } ]

#@pytest.fixture
#def tranzact_list(tranzaction_list):
     #return tranzaction_list


#tranzactions_list = [
#
 #       {
   #         "id": 939719570,
  #          "state": "EXECUTED",
  #          "date": "2018-06-30T02:08:58.425572",
   #         "operationAmount": {
  #              "amount": "9824.07",
 #               "currency": {
 #                   "name": "USD",
  #                  "code": "USD"
  #              }
  #          },
  #          "description": "Перевод организации",
   #         "from": "Счет 75106830613657916952",
  #          "to": "Счет 11776614605963066702"
  #      },
 #       {
  #          "id": 142264268,
  #          "state": "EXECUTED",
  #          "operationAmount": {
  #              "amount": "79114.93",
  #              "currency": {
  #                  "name": 'USD',
  #                  "code": "SD"
 #               }
#            },
 #           "description": "Перевод со счета на счет",
 #           "from": "Счет 19708645243227258542",
 #           "to": "Счет 75651667383060284188"
 #       },
 #           {
 #           "id": 142264268,
 #           "state": "EXECUTED",
  #          "date": "2019-04-04T23:20:05.206878",
 #           "operationAmount": {
 #               "amount": "79114.93",
  #              "currency": {
 #                   "name": 'USD',
 #                   "code": "U"
 #               }
 #           }



