"""
Operacje na łańcuchach znakowych, formatowanie i konwersja typów
"""

napis = "Wiek: " + str(18)
print(napis)

# Zamiana znaków w tekście
print(napis.replace("W", "w"))

print(napis.lower())

print(napis.upper())

# Formatowanie tekstu (stara metoda Python 2.7)
napis = "Liczba %f to %s" % (3.14, "pi")
print(napis)

# Formatowanie tekstu (nowa metoda Python 3.x)
napis = "Liczba {0} to {1}".format(3.14, "pi")
print(napis)

# Konwersja typu tekstowego na typ liczbowy
a = '5'
b = 7
print(int(a) + b)

# Konwersja typu liczbowego na typ tekstowy
a = '6'
b = 9
print(a + repr(b))
print(a + str(b))
