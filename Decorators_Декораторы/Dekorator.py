"""
Написал 3 функции создания положительных четных чисел от 0 до N.
Определил через декоратор время работы этих функций
"""
import time


def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        res = func(*args, **kwargs)
        return f"{res} \n</h1>"

    return inner


def getTime(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print(f"Время выполнения {end - start}")
        return (res)

    return wrapper


@header
@getTime  # getEvenCompreh = getTime(getEvenCompreh)
def getEvenCompreh(num):
    return [item for item in range(num + 1) if item % 2 == 0]


@getTime
def getEvenFor(num):
    res = []
    for item in range(num + 1):
        if item % 2 == 0:
            res.append(item)
    return res


@getTime
def getEvenWhile(num):
    res = []
    while num > -1:
        if num % 2 == 0:
            res.append(num)
        num -= 1
    return res


print(getEvenCompreh(20))
print(getEvenFor(20))
print(getEvenWhile(20))
