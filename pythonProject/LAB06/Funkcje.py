# Funkcje

# 1.Przykłady funkcji

"""
Funkcje
"""


def wyswietl(a, b):
    print(a, b)


def dodaj(a, b):
    return a + b


wyswietl(5, 8)
c = dodaj(4, 6)
print(c)

print()

# 2.Funkcje wewnętrzne

"""
Funkcje wewnętrzne
"""


def funkcja1(a):
    print(a)


def funkcja2():
    print(a * 2)

    funkcja2()


funkcja1(5)


def oblicz(a, b):
    print(a * b)


test = oblicz
test(2, 4)

a = 10
if a < 5:
    def funkcja():
        print('liczba mniejsza od 5')
else:
    def funkcja():
        print('liczba większa lub równa 5')

funkcja()

print()

# 3.Argumenty funkcji

"""
Argumenty funkcji
"""


# Przykład 1
def wyswietl(a, b, c):
    print(a, b, c)


wyswietl(5, 10, 15)
wyswietl(2, c=6, b=4)


# Przykład 2
def wyswietl2(a, b=4, c=8):
    print(a, b, c)


wyswietl2(2)
wyswietl2(1, 2)
wyswietl2(3, c=6)


# Argumenty dowolne
def wypisz(*arg):
    print(arg)


def wypisz2(**arg):
    print(arg)


wypisz(1, 2, 3)
wypisz2(a=1, c=3)

print()

# 4.Zakres zmiennych

"""
Zakres zmiennych
"""

# Zakres loklany
x = 5


def wypisz1(a):
    x = a
    print(x)


wypisz1(2)
print(x)

# Zakres globalny
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





