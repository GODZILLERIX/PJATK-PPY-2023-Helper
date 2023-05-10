"""
Lab09 - Wyjątki
"""

def pobierz(sek, ind):
    return sek(ind)

pliki = ["czarny_kot.txt", "nowe-plik.txt"]
ind = 2

try:
    print(pobierz(pliki, ind))
except IndexError:
    print("wystąpił bład")
