def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


""" Использован метод рекурсии"""
a = int(input("Enter the sequence number "))
print("Fibonacci number with ordinal number - " + str(a), "will be equal", fib(a))
