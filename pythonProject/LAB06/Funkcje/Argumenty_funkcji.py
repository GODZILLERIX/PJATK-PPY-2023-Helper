"""
Lab06 - argumenty funkcji
"""


# Przyklad 1
def wyswetl(a, b, c):
    print(a, b, c)


wyswetl(5, 10, 15)
wyswetl(5, c=6, b=4)


# Przyklad 2
def wyswietl2(a, b=4, c=8):
    print(a, b, c)


wyswietl2(2)
wyswietl2(1, 2)
wyswietl2(3, c=6)


# argumenty dowolne
def wypisz1(*arg):
    print(arg)


def wypisz2(**arg):
    print(arg)


wypisz1(1, 2, 3)
wypisz2(a=1, c=3)


# kolejnosc arguentow
def wypisz3(a, b, c=3, *args, **kwargs):
    print(a, b, c, args, kwargs)


wypisz3(1, 2)
wypisz3(2, 3, 4, 5, 6, e=5, f=6)


# przekaywanie argumentow za pomoca słowa kluczowego
def wypisz4(a, b, *args, c, d):
    print(a, b, args, c, d)


wypisz4(1, 2, 3, 4, c=5, d=7)
