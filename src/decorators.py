from datetime import datetime
from functools import wraps


def log(filename:[str] = None):

    """   Функция декоратор с параметрами   """
    def decor(func):
        @wraps(func)
        def wrapp(*args,**kwargs):
            try:
                start_of_func = datetime.now()
                start_of_func_= start_of_func.strftime('%Y-%m-%d %H:%M:%S\n')
                res = func(*args,**kwargs)
                if filename :
                     with open('logs.txt','a',encoding='utf-8') as file:
                         file.write(f'{func.__name__} ok\n')
                if not filename:
                    print(f'{func.__name__} ok\n')
                return res
            except Exception as e:
                if filename:
                    with open('logs.txt', 'a', encoding='utf-8') as file:
                        file.write(start_of_func_)
                        file.write(f'error{type(e).__name__}\n')
                if not filename :
                    print(f'error {type(e).__name__}')
                    print(start_of_func_)
                    res=None
                    return res


        return wrapp

    return decor


@log()#(filename ='logs.txt')
def functt(a):

    """ Функци """

    for i in range(a):
        print(a+c)
    return a

functt(50)
