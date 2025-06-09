from datetime import datetime
from functools import wraps


def log(filename:[str] = None):

    """   Функция декоратор с параметрами   """
    def decor(func):
        @wraps(func)
        def wrapp(*args,**kwargs):
            try:
                start_of_func = datetime.now()
                start_of_func_= start_of_func.strftime('%Y-%m-%d %H:%M:%S:%f\n')
                end_of_func = datetime.now()
                end_of_func_ = end_of_func.strftime('%Y-%m-%d %H:%M:%S:%f\n')
                res = func(*args,**kwargs)
                if filename :
                     with open('logs.txt','a',encoding='utf-8') as file:
                         file.write(start_of_func_)
                         file.write(f'{func.__name__} ok')
                         file.write(end_of_func_)
                if not filename:
                    print(f'{func.__name__} ok')
                    print(end_of_func)
                    print(end_of_func_)
                return res
            except Exception as e:
                if filename:
                    with open('logs.txt', 'a', encoding='utf-8') as file:
                        file.write(f'error{type(e).__name__}')
                        file.write(start_of_func_)
                        file.write(end_of_func_)
                if not filename :
                    print(f'error {type(e).__name__}')
                    print(end_of_func_)
                    print(start_of_func_)
                    res = None
                    return res


        return wrapp

    return decor


@log  ()#(filename ='logs.txt')
def functt(a):

    """ Функци """

    for i in range(a):
        print(a)
    return a+25

functt(50)
