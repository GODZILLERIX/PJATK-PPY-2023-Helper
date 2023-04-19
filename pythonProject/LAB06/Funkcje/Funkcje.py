"""
Lab06 - Funkcje
"""


# Przyklady funkcji

def wyswietl(a, b):
    print(a, b)


def dodaj(a, b):
    return a + b


wyswietl(5, 8)
c = dodaj(4, 6)
print(c)


# Funkcje wewnetrzne

def funkcja1(a):
    print(a)

    def funkcja2():
        print(a * 2)

    funkcja2()


funkcja1(5)


def oblicz(a, b):
    print(a + b)


test = oblicz
test(2, 4)

a = 10
if a < 5:
    def funkcja():
        print("liczba mniejsza od 5")
else:
    def funkcja():
        print("liczba wieksza lub rowna 5")

funkcja()