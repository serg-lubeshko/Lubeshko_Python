""" Написать функцию для вычисления суммы всех элементов вложенных списков.
Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элменетов - 34
Функция должна быть рекурсивной, то есть она должна обходить каждый элемент списка и
вызывать саму себя, если текущий элемент так же является списком. """

import functools


def unpack_list(list_):
    a = []
    for i in list_:
        if type(i) == list or type(i) == tuple:
            b = unpack_list(i)
        else:
            b = [i]
        a.extend(b)
    return a


""" Метод рекурсии. Данная функция позволяет распаковать список в списке в один  """

print("Sum of list items ", sum(unpack_list([1, 2, [2, 4, [[7, 8], 4, 6]]])))
print("Multiplication of list items", functools.reduce(lambda x, y: x * y, unpack_list([1, 2, [2, 4, [[7, 8], 4, 6]]])))
