#s22347 Arseniy Patapenka

# Zadanie 1 - 1 pkt
# ---------------------------------------------------------------------
# Wypisz na ekranie nicki 10 najlepszych graczy z dowolnej dyscypliny.
# Użyj tylko jednej instrukcji print i wypisz je w jednym wierszu

Formula1 = ["Max Verstappen","Lewis Hamilton","Niko Rosberg","Fernando Alonso","Checo Perez","Charles Leclerc","Sebastian Vettel","Felipe Massa","Michael Schumacher","Kimi Raikkonen"]

print(Formula1)

print()

# Zadanie 2 - 1 pkt
# ------------------------------------------------------------------------
# Zmodyfikuj zadanie 1 w taki sposób aby nicki były wypisywane w osobnych
# wierszach. Również wykorzytaj tylko jendą instrukcję print.

Formula1 = ["Max Verstappen", "Lewis Hamilton", "Niko Rosberg", "Fernando Alonso", "Checo Perez", "Charles Leclerc", "Sebastian Vettel", "Felipe Massa", "Michael Schumacher", "Kimi Raikkonen"]

for driver in Formula1:
    print(driver)

print()


# Zadanie 3 - 3 pkt
# ---------------------------------------------------------------
# Napisz skrypt rysujący z gwiazdek * prostokąt o długości a = 3
# i szerokości b = 4. Spraw aby skrypt obliczał i wyświetlał pole
# oraz obwód tego prostokąta

a = 3
b = 4

for i in range(a):
    for k in range(b):
        print("*", end=" ")
    print()

pole = a * b
obwod = 2 * (a + b)
print("Pole:", pole)
print("Obwód:", obwod)

print()


# Zadanie 4 - 5 pkt
# ---------------------------------------------------------------
# Coca-Colę piją obecnie tylko zamożni obywatele. Napisz skrypt,
# w którym przygotowujesz raport pokazujący zmiany cen tego
# popularnego napoju po dodaniu nowego podatku cukrowego:
#
# Ceny przed: 3.69, 4.5, 3.6, 4.0, 3.99, 3.59
# Ceny po: 4.5, 5.5, 4.69, 4.99, 4.00
# Twoim zadaniem jest podanie informacji o:
#
# a) najwyższej cenie po nałożeniu podatku,
#
# b) najniższej cenie biorąc pod uwagę wszystkie ceny (przed i po),
#
# c) średniej cenie przed podwyżką cen,
#
# d) średniej cenie po dodaniu nowego podatku.

Przed = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]

Po = [4.5, 5.5, 4.69, 4.99, 4.0]

print("Raport: ")
najwyzsza_cena_po = max(Po)
print("Najwyższa cena po: ", najwyzsza_cena_po)

najnizsza_cena = min(Przed + Po)
print("Najniższa cena: ", najnizsza_cena)

srednia_przed = sum(Przed) / len(Przed)
print("Średnia cena przed: ", srednia_przed)

srednia_po = sum(Po) / len(Po)
print("Średnia cena po: ", srednia_po)

print()


# Zadanie 5 - 2 pkt
# ------------------------------------------------------------------------
# Napisz skrypt tworzący słownik, którego kluczami będą nicki z zadania 1,
# a wartościami liczba pkt.

thisdict = {
  "Max Verstappen": 100,
  "Lewis Hamilton": 222,
  "Niko Rosberg": 33,
  "Fernando Alonso": 40,
  "Checo Perez": 57,
  "Charles Leclerc": 76,
  "Sebastian Vettel": 57,
  "Felipe Massa": 87,
  "Michael Schumacher": 69,
  "Kimi Raikkonen": 120
}
print(thisdict)

print()


# Zadanie 6 - 4 pkt
# -------------------------------------------------------------------------
# Zmodyfikuj zadanie 5 w taki sposób aby stworzyć słownik składany.
# Wartościami słownika będą listy słowników zawierające pary (data: punkty)

# Tworzymy słownik składany z listami słowników

thisdict2 = {
  "Max Verstappen": [{'2022-03-04': 25}, {'2022-01-02': 25}, {'2022-01-09': 50}],
  "Lewis Hamilton": [{'2022-03-08': 100}, {'2022-01-22': 100}, {'2022-01-08': 22}],
  "Niko Rosberg": [{'2022-02-04': 11}, {'2022-04-02': 11}, {'2022-05-09': 11}],
  "Fernando Alonso": [{'2022-10-04': 10}, {'2022-09-02': 10}, {'2022-12-09': 20}],
  "Checo Perez": [{'2022-03-15': 25}, {'2022-01-14': 25}, {'2022-01-13': 7}],
  "Charles Leclerc": [{'2022-03-16': 35}, {'2022-01-17': 35}, {'2022-01-18': 6}],
  "Sebastian Vettel": [{'2022-03-11': 25}, {'2022-01-12': 25}, {'2022-01-19': 7}],
  "Felipe Massa": [{'2008-03-15': 40}, {'2008-01-14': 40}, {'2008-01-13': 7}],
  "Michael Schumacher": [{'2006-03-15': 30}, {'2006-01-14': 30}, {'2006-01-13': 9}],
  "Kimi Raikkonen": [{'2005-03-20': 40}, {'2005-01-23': 40}, {'2005-01-13': 40}]
}
print(thisdict2)

print()


# Zadanie 7 - 4 pkt
# --------------------------------------------------------------------------------
# Napisz skrypt wyświetlający wszystkie liczby całkowite z przedziału od 20 do 80
# podzielne przez dowolną liczbę k, którą podaje użytkownik. Liczby powinny być
# wyświewtlone w postaci listy lub słownika. Decyduje użytkownik skryptu.

k = int(input("Podaj liczbę: "))

wynik = []
if input("W jakiej postaci zrobić wynik? (słownik/list): ") == "słownik":
    wynik = {}

for i in range(20, 81):
    if i % k == 0:
        if type(wynik) == list:
            wynik.append(i)
        else:
            wynik[str(i)] = i

if type(wynik) == list:
    print(wynik)
else:
    type(wynik) == dict
    print(wynik)


# Zadanie 8 - 4 pkt
# --------------------------------------------------------------------------
# Zmodyfikuj zadanie 7 w taki sposób aby użytkownik mógł podać zakres liczb
# oraz ilość dowolnych liczb k.
# Wyniki wyświetl w postaci słownika (k: liczby całkowite)(you need to create

a = int(input("Podaj początek zakresu: "))
b = int(input("Podaj koniec zakresu: "))
n = int(input("Podaj długość lista wartośćiej k: "))

list = []
for i in range(n):
    element = int(input("Podaj wartośći k: "))
    list.append(element)

    for element in list:
        res = {}
        for i in range(a, b+1):
            if i % element == 0:
                if element not in res:
                    res[element] = []
                res[element].append(i)

        print(res)


# Zadanie 9 - 3 pkt
# --------------------------------------------------------------------------
# Napisz skrypt, który dla trzech liczb a, b i c wprowadzonych z klawiatury
# sprawdza, czy są to trójki pitagorejskie.
# Dodatkowo należy założyć, że a > 0, b > 0 oraz c > 0.

a = int(input("Napisz pierwszą liczbę: "))
b = int(input("Napisz drugą liczbę: "))
c = int(input("Napisz trzecią liczbę: "))

if a > 0 and b > 0 and c > 0:
    if a**2 + b**2 == c**2:
        print("Wpisane liczby to są trójki pitagorejskie.")
    else:
        print("Wpisane liczby to są nie trójki pitagorejskie.")
else:
    print("Wartości powinny być więcej niż 0")

print()


# Zadanie 10 - 3 pkt
# -------------------------------------------------------------------------------
# Napisz skrypt, który korzystając z instrukcji while, sumuje liczby nieparzyste
# w przedziale od 1 do 100.

num = 1
sum = 0

while num < 101:
    if num % 2 == 1:
       sum = sum + num
    num = num + 1
print("Suma liczb nieparzystych w przedziale od 1 do 100 równa się:", sum)









































