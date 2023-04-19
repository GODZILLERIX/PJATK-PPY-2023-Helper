"""
Lab06 - zakres zmiennych
"""

# zakres lokalny
x = 5


def wypisz1(a):
    x = a
    print(x)


wypisz1(2)
print(x)

# zakres globalny
y = 4


def wypisz2(b):
    global y
    y = b
    print(y)


wypisz2(8)
print(y)


# zakres nonlocal
def funkcja1():
    a = 5
    print(a)

    def funkcja2():
        nonlocal a
        a = 10

    funkcja2()
    print(a)


funkcja1()
