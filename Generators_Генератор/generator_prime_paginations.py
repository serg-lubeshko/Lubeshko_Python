"""
Функцию-генератор, иммитирующую работу пагинатора в веб-фреймворках.
"""


def pagination(lst, num=3):
    for cur_point in range(0, len(lst), num):
        pagination = lst[cur_point:cur_point + num]
        yield pagination


fun = pagination(['hello', 'world', 'this', 'is', 'my', 'new', 'generator', 'task'])
print(next(fun))
print(next(fun))
print(next(fun))