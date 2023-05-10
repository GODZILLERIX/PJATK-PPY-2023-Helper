"""
Lab09 - obsługa plików - zapis
"""

plik1 = open("nowe-plik.txt", mode = "w", encoding = "utf-8")
plik1.write("Przekładowy tekst")
plik1.close()

plik2 = open("nowe-plik.txt", mode = "w", encoding = "utf-8")
p1 = plik2.write("Przekładowy tekst")
plik2.close()
print(p1)

plik3 = open("nowe-plik.txt", mode = "a", encoding = "utf-8")
plik3.write("\n Drugi wiersz\n")
plik3.close()

with open ("nowe-plik.txt", mode = "r", encoding = "utf-8") as plik4:
    print(plik4.read())