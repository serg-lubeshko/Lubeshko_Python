"""
Генератор последовательности Фибоначчи (генератор может выдавать бесконечное количество элементов)
"""


def create_row_fibonacci():
    num_pre = 0
    num_next = 1
    while True:
        num_pre, num_next = num_next, num_pre + num_next
        yield num_pre


fun = create_row_fibonacci()

for item in range(10):
    print(next(fun))
