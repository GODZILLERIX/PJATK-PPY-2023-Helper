"""
Lab04 - instrukcje warunkowe
"""

# Przykłady prostych instrukcji warunkowych

if 1 < 2:
    print("prawda")

if True:
    print("prawda")

if "napis":
    print("prawda")

if 1:
    print("prawda")

if None:
    print("prawda")

x = True
y = False

if x and y:
    print("prawda")

if x or y:
    print("prawda")

print()

# Przykąłdy zagnieżdżonych instrukcji warunkowych
a = -1

if a < 0:
    print("Czerwony")
    if a != -20:
        print("Bingo!!! " * 3)

print()

# Przykłady bardziej zaawansowanych instrukcji warunkowych
wybor = int(input("Podaj dowolną liczbę całkowitą: "))

if wybor < 0:
    print("Czerwony")
elif wybor == 0:
    print("Biały")
else:
    print("Zielony")

if wybor < 0:
    print("czerwony")
else:
    print("zielony")

if 10 <= wybor <= 100: # wybor >= 10 and wybor <= 100
    print("<10 - 100>")
else:
    print("zły zakres")
