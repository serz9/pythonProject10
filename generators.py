
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


def filter_by_carrency(tranzactions_list: list[str], currency: [str]):
    """   функция фильтрации   """

    res = (i for i in tranzactions_list if i['operationAmount']['currency']['code'] == currency)
    for n in res:
        yield n


filter_run = filter_by_carrency(tranzactions_list, 'USD')
for tranzaction in filter_run:
    print(next(filter_run))
    print(tranzaction)

filter_by_carrency(tranzactions_list, 'USD')
#def filter_by_carrency( tranzactions_list: list[dict], currency: [str] ):

   # """    функция фильтрации   """

    #res_ = [i for i in tranzactions_list if i['operationAmount']['currency']['code'] == currency]
    #res = (i for i in tranzactions_list if i['operationAmount']['currency']['code'] == currency)

 ##for i in range(0,len(res_)):
        ##print(next(res))
    #for tranzaction in res:
       # print(next(res))
        #print(tranzaction)

#filter_by_carrency(tranzactions_list,'USD')
#filter_gen = filter_by_carrency()

#def fltr( trnlist):
    #for i,x in inumerate(trnlist):
        #yield x

#i = (x for x in trnlist)
#print(i)
#filter_by_carrency(['w','s','d'],'df')
#print(res())
#next(filter_by_carrency(i,carrency)
#def get_number(number):

    #"""функция возвращает скрытый номер банковской карты"""

    #number = (
           # len(number[0:4])*"X"
            #+ " "
            #+ len(number[4:6])* "X"
            #+ len(number[6:8]) * "X"
            #+ " "
            #+ len(number[8:12])* "X"
            #+ " "
            #+ number[12:16]
    #)
    #print(number)
    #return number
def transaction_descriptions(tranzactions_list):

    """    описание транзакций   """

    for i in tranzactions_list:
        res = (i['description'] for i in tranzactions_list)
        print(next(res))

#card_number = str(number).zfill(16)
#formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])

transaction_descriptions(tranzactions_list)

def get_number(number):

    """   функция  преобразует номера карт в формат XXXX XXXX XXXX 4564   """

    card_number = str(number).zfill(16)
    formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
    print(formatted_card_number)
    return formatted_card_number
def card_number_generator(start, end):

    """   функция генератор номеров карт   """

    global number
    for j in range(start, end + 1):
        count_0 = "0" * (16 - len(str(j)))
        number = count_0 + str(j)
        get_number(number)

card_number_generator(1,55)


#def get_number(number):
    #card_number = str(number).zfill(16)
    #formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
    #print(formatted_card_number)
    #return formatted_card_number

#card_number_generator(1,333333)
#def get_number(number):

