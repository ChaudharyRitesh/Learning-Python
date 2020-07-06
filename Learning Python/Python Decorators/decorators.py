# higher order function
from time import time
# def greet(func):
#     func()

# def another_greeting():
#     def func():
#         return 5
#     return func


# Decorators

# def my_decorator(func):
#     def wrapper_func(*args, **kwargs):
#         print('**********')
#         func(*args, **kwargs)
#         print('**********')
#     return wrapper_func


# @my_decorator
# def hello(greeting, emoji='😃'):
#     print(greeting, emoji)

# hello('hello')

def performaance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = fn(*args, **kwargs)
        t2 = time()
        print (f'it took {t2-t1} second')
        return res
    return wrapper


@performaance
def long_time():
    for i in range(100000000):
        i*5

long_time()