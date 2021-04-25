"""
генератор последовательности простых чисел (генератор может выдавать бесконечное количество элементов)
"""

def create_prime_number():
    list_nums = []
    num_prime = 2
    while True:
        for list_num in list_nums:
            if num_prime % list_num == 0:
                break
        else:
            list_nums.append(num_prime)
            yield num_prime
        num_prime += 1


fun = create_prime_number()

for _ in range(20):
    print(next(fun))
