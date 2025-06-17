from datetime import datetime
from functools import wraps
from typing import Optional





def log(filename:Optional[str]):

    """   Декоратор фиксирует роботу функции  консоль или в файл log.txt   """
    def decor(func):
        @wraps(func)
        def wrapp(*args,**kwargs):
            try:
                start_of_func = datetime.now()
                start_of_func_ = start_of_func.strftime('%Y-%m-%d %H:%M:%S:%f\n')
                end_of_func = datetime.now()
                end_of_func_ = end_of_func.strftime('%Y-%m_%d %H:%M:%S:%f\n')
                res = func(*args,**kwargs)
                if filename :
                     with open('logs.txt','a',encoding='utf-8') as file:
                         file.write(f'{func.__name__} ok\n')
                         file.write(start_of_func_)
                         file.write(end_of_func_)
                if not filename:
                    print(f'{func.__name__} ok\n')
                    print(start_of_func_)
                    print(end_of_func_)
                    return res
            except Exception as e:
                if filename:
                    with open('logs.txt', 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__}\n')
                        file.write(f'{type(e).__name__}\n')
                        file.write(start_of_func_)
                        file.write(end_of_func_)
                if not filename:
                    print(f'{func.__name__}')
                    print(f'error {type(e).__name__}\n')
                    print(start_of_func_)
                    print(end_of_func_)
                    res = None
                    return res


        return wrapp

    return decor


@log(filename ='logs.txt')
def functt(a):

    """ Функции """

    for i in range(a):
        print(a)
    return a

functt(50)


