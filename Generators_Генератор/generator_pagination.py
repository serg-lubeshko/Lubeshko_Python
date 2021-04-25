"""
Функция-генератор, иммитирующую работу пагинатора в веб-фреймворках. Функция принимает 2 параметра: список элементов
подлежащих пагинации и размер части списка. Если размер последней части меньше размера пагинации, выводить
количество последних элементов соответствующих размеру пагинации.
"""


def func(lst, num_pagin=3, fill_last=True):
    cur_point = 0
    while fill_last:
        pagination = lst[cur_point:cur_point + num_pagin]
        cur_point = cur_point + num_pagin
        if pagination:
            if len(pagination) < num_pagin:
                fill_last = False
                pagination = list(reversed(lst[-1:-num_pagin - 1:-1]))
            yield pagination


fun = func(['hello', 'world', 'this', 'is', 'my', 'new', 'generator', 'task'])

print(next(fun))
print(next(fun))
print(next(fun))
print(next(fun))
