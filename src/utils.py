import os.path
import json
from dotenv import load_dotenv

load_dotenv()
def jsn_date(path_)  :

    """   Функция проверки данных   """

    date_path = path_
    data=[]
    try:
        if not os.path.isfile(date_path):
            print(data)
            return data
        else:
            with open(date_path,'r',encoding='utf-8') as file:
                data_=json.load(file)
                print(data_)

            if isinstance(data_,list):
                print('данные являются списком')
                if all(isinstance(item, dict) for item in data_):
                    print('файл является списком словарей ')
                else:
                    return data
            if len(data_)==0:
                print(data)
                return(data)

            return data_
    except Exception as e :
        print(f'ошибка {e}')


jsn_date(r'C:/Users/serzh/PycharmProjects/pythonProject10/date/operations.json')


