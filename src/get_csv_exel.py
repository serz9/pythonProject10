

import pandas as pd


import csv

def read_csv_transactions(path_):

    """   Функция читает csv файлы   """
    try:
        csv_dict = []
        with open(path_, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            header_ = next(reader)
            for row in reader:
                csv_str = dict(zip(header_, row))
                csv_dict.append(csv_str)
            print(csv_dict)
            return csv_dict
    except Exception as e:
        print(f"ошибка {e} ")

#read_csv_transactions(r'C:\\Users\\serzh\\PycharmProjects\\pythonProject10\\src\\transactions.csv')
def read_excel_transactions(path_):

    """   Функция читает excel файлы   """
    try:
        excel_dicts = []
        reader = pd.read_excel(path_, sheet_name='Лист 1')
        for index, row in reader.iterrows():
            head_ = reader.columns.tolist()
            excel_dict = dict(zip(head_, row))
            excel_dicts.append(excel_dict)
        print(excel_dicts)
        return excel_dicts
    except Exception as e :
        print(f"ошибка {e} ")

#read_excel_transactions(r'C:\\Users\\serzh\\PycharmProjects\\pythonProject10\\src\\transactions_excel.xlsx')

if __name__ == "__main__ " :

    read_csv_transactions(r'C:\\Users\\serzh\\PycharmProjects\\pythonProject10\\src\\transactions.csv')
    read_excel_transactions(r'C:\\Users\\serzh\\PycharmProjects\\pythonProject10\\src\\transactions_excel.xlsx')



