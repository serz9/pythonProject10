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
                    "name": 'USD',
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]


def filter_by_currency(tranzactions_list: list[str], currency: [str]):

    """   Функция фильтрации   """

    res = (i for i in tranzactions_list if i['operationAmount']['currency']['code'] == currency)
    for i in res:
        yield i


filter_run = filter_by_currency(tranzactions_list, 'USD')
for tranzaction in filter_run:
    print(tranzaction)

filter_by_currency(tranzactions_list, 'USD')


def transaction_descriptions(tranzactions_list):

    """   Описание транзакций   """

    #res = (i['description'] for i in tranzactions_list)
    for i in tranzactions_list:
        yield i['description']


res_ = transaction_descriptions(tranzactions_list)
for n in tranzactions_list:
    print(next(res_))


#def get_number(number):

    #"""   Функция  преобразует номера карт в формат 3432 3432 4343 4564   """

    #card_number = str(number).zfill(16)
    #global formatted_card_number
    #formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
    #print(formatted_card_number)
    #yield formatted_card_number

#def card_number_generator(start, end):

   # """   Функция генератор номеров карт   """

    #global number
    #for j in range(start, end + 1):
        #count_0 = "0" * (16 - len(str(j)))
        #number = count_0 + str(j)
        #next(get_number(number))


#card_number_generator(123,125)
def card_number_generator(start,end):

    """   Функция  преобразует номера карт в формат 0000 0000 0043 4564   """

    for number in range(start, end+1) :
        card_number = str(number).zfill(16)
        formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
        yield formatted_card_number

#res = card_number_generator(1,5)

all_numbers = card_number_generator(1,5)

for i in all_numbers:
    print(i)