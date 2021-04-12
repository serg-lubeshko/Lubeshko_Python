#  coding: utf-8
def pol(x):
    if len(x) == 1:
        return True
    elif x[0] != x[-1]:
        return False
    return pol(x[1:-1])

print(pol('шалаш'))
