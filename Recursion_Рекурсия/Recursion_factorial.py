def factorial(n):
    if n == 0:
        return 1

    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


""" Использован метод рекурсии"""

a = int(input("Enter number "))
print("Factorial for number - " + str(a), "will be equal", factorial(a))
