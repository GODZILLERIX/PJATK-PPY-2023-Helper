"""
Lab03 - krotki
"""

# Tworzenie krotki
krotka1 = ()
print(krotka1)

krotka2 = (1,)
print(krotka2)

krotka2 = 1,
print(krotka2)

krotka3 = 1, 3.14, "PJATK"
print(krotka3)

krotka4 = 1, 3.14, [2, 3], 1
print(krotka4)

napis = "abcdef"
print(tuple(napis))

# Indeksowanie krotkek
print(krotka3[0])
print(krotka3[:2])

# Operacje na krotkach
print(krotka4.count(1))
print(krotka4.index(1))
