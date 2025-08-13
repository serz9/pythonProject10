import os
import json
from dotenv import load_dotenv
load_dotenv()


dt=os.path.exists('date/operations.json')
print(dt)
def jsn_date(path_)  :
    date_path = path_

    with open(date_path,'r') as file:

        if not os.path.isfile(date_path):
            return []
        if not isinstance(file, list):
            return []
        if len(file)==0:
            print([])
            return []



jsn_date(' date/operations.json ')