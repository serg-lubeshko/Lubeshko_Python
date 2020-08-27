""" Написать функцию для вычисления суммы всех элементов вложенных списков.
Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элменетов - 34
Функция должна быть рекурсивной, то есть она должна обходить каждый элемент списка и
вызывать саму себя, если текущий элемент так же является списком. """

import functools


# _______________________________________________________________________________________
def unpack_list(list_):
    a = []
    for i in list_:
        if type(i) == list or type(i) == tuple:
            b = unpack_list(i)
        else:
            b = [i]
        a.extend(b)
    return a


""" Метод рекурсии. Данная функция позволяет распаковать список в списке в один. После чего можно работать с обычным списком """


# _______________________________________________________________________________________
def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el


""" Вместо lambda можно использовать reducer_func(el_prev, el), где
# el_prev — предшествующий элемент
# el — текущий элемент
 """
# _______________________________________________________________________________________

print("Expanded list ", (unpack_list([1, 2, [2, 4, [[7, 8], 4, 6]]])))
print("Sum of list items ", sum(unpack_list([1, 2, [2, 4, [[7, 8], 4, 6]]])))

print("My example 1-lambda. Multiplication of list items",
      functools.reduce(lambda x, y: x * y, unpack_list([1, 2, [2, 4, [[7, 8], 4, 6]]])))

print("My example 2-reducer_func. Multiplication of list items",
      functools.reduce(reducer_func, unpack_list([1, 2, [2, 4, [[7, 8], 4, 6]]])))

print("My example 3-filter. Even elements from the list",
      list(filter(lambda x: x % 2 == 0, unpack_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))))
