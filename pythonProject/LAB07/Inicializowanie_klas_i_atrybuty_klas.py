"""
Inicializowanie klas i atrybuty klas
"""

class Zwierz:
    """Pierwsza klasa"""

    rodzaj = "zwierze"

    def __int__(self, gatunek, wiek):
        self.gatunek = gatunek
        self.wiek = wiek

    def podaj_gatunek(self):
        print("lis")


# instancje klas
a = Zwierz("lis", 5)
b = Zwierz("python", 2)

#wyświetlenie wartości atrybutów
print(a.gatunek, a.wiek)
print(b.gatunek,b.wiek)

# definiowanie atrybutów instancji poza klasą
b.dlugosc=10
print(b.dlugosc)
#print(a.dlugosc)

# wyświetlenie atrybutów wspólnych dla obiektów klas
print(a.rodzaj, b.rodzaj)

# zmiana wartości atrybutów
b.dlugosc = 11
print(b.dlugosc)
a.wiek = 6
print(a.wiek)

#atrybuty specialne - nie wymagają deklaracji
#atrybuty klasy w formie słownika
print(a.__dict__)
print(b.__dict__)

# opis klasy
print(Zwierz.__doc__)
print(a.__doc__)