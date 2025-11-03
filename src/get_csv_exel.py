import csv
import get_csv_exel.py
#pandas as pd
#def csv_read():

with open('transactions.csv') as file :
    reader=csv.reader(file)
    for row in reader:
        print(row)

csv_read()