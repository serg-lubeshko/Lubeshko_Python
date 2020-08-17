# объявление функции
def is_password_good(password):

    if (any(i.isupper() for i in password) and any(i.islower() for i in password) and any(i.isdigit() for i in password) and
            len(password) >= 8):
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
