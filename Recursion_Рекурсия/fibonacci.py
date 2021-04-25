"""
Вариант 1. Рекурсия

"""
def fib1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib1(n - 2) + fib1(n - 1)

print((fib1(15)), "вариант 1")

"""
Вариант 2. Рекурсия
Мне очень нравиться метод использования словаря, где № своя сумма

"""

dict_sums = {0: 0, 1: 1}
def fib2(number):
    if number in dict_sums:
        return dict_sums[number]
    dict_sums[number] = fib2(number - 1) + fib2(number - 2)
    return dict_sums[number]

print((fib2(15)), "вариант 2")
