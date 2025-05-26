from functools import wraps
from datetime import datetime


def log (filename: [str] = None):
    def decor(func):
        @wraps(func)
        def wrapp(*args,**kwargs):
            try :
                start_of_func = datetime.now()
                res = func(*args,**wargs)
                end_of_func = datetime.now()
                if filename :
                     with open ('logs.txt','a',encoding='utf-8') as file:
                         file.write(f'{function.__name__}ok\n')
                else:
                    print(f'{function.__name__}ok\n')
            except Exception as e:
                if filename :
                    with open('logs.txt', 'a', encoding='utf-8') as file:
                        file.write(start_of_func, end_of_func,type(e))
                if filename == False:
                    print(f'error{e}')
                    print(start_of_func)
                    print(end_of_func)
                return res

            return wrapp

        return decor


@log#(#filename ='logs.txt')
def functt(a):
    #""" Функци """
    #for i in range(a):
        #print(a)
    return a

functt(50)
