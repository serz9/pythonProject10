tranzactions_list = [

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
                    "name": 'RUB',
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]


def filter_by_currency(tranzactions_list: list[str], currency: [str]):

    """   Функция фильтрации   """

    res = (i for i in tranzactions_list if i['operationAmount']['currency']['code'] == currency)
    return res


#filter_run = filter_by_currency(tranzactions_list, 'USD')
#for tranzaction in filter_run:
    #print(tranzaction)


def transaction_descriptions(tranzactions_list):

    """   Описание транзакций   """

    res_ = (i['description'] for i in tranzactions_list)
    for i in tranzactions_list:
        yield i['description']


    res_ = transaction_descriptions(tranzactions_list)
    for n in tranzactions_list:
        print(next(res_))


def card_number_generator(start,end):

    """   Функция  преобразует номера карт в формат 0000 0000 0043 4564   """

    for number in range(start, end+1) :
        card_number = str(number).zfill(16)
        formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
        yield formatted_card_number

all_numbers = card_number_generator(1,5)

for i in all_numbers:
    print(i)


if __name__ == '_main__':

    filter_run = filter_by_currency(tranzactions_list, 'USD')
    for tranzaction in filter_run:
        print(tranzaction)


    filter_by_currency(tranzactions_list, 'USD')
    res_ = transaction_descriptions(tranzactions_list)
    for n in tranzactions_list:
         print(next(res_))


    all_numbers = card_number_generator(1,5)
    for i in all_numbers:
        print(i)
