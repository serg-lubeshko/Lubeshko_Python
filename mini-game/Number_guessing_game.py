import random


def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False


play = True
while play:
    print("""Добро пожаловать в "Числовую угадайку" """)

    n = int(input("Введите предел загадываемого числа"))
    num_random = random.randint(1, n)                       # Generate any number

    print(f"Введите число от 1 до {n}")
    count = 1

    while True:
        a = input()
        if not is_valid(a):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue
        else:
            if int(a) < num_random:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                count += 1
                continue
            elif int(a) > num_random:
                print("Ваше число больше загаданного, попробуйте еще разок")
                count += 1
                continue
            elif int(a) == num_random:
                print("Вы угадали, поздравляем!!!", "Количество попыток -", count)

                break
    print("Хотите еще сыграть?")
    if input("Если 'ДА' нажмите - 1") == "1":
        play = True
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        play = False
