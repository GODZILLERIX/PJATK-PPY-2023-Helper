"""
Lab03 - Zbiory
"""

# Tworzenie zbirów
zb1 = {}
print(zb1)

zb1 = {1, 2, 3}
print(zb1)

zb2 = set((3, 5, 7, 2))
print(zb2)

print(zb2.pop())
print(zb2)

# Opercje na zbiorach

print(zb1.union(zb2))
print(zb1 | zb2)

print(zb1.intersection(zb2))
print(zb1 & zb2)

print(zb1.difference(zb2))
print(zb1 - zb2)

print(zb2.difference(zb1))
print(zb1 - zb2)

print(zb1.symmetric_difference(zb2))
print(zb1 ^ zb2)

zb3 = {1, 4, 7, 3.14}
print(zb3)

zb3.add(6.18)
print(zb3)

zb3.remove(3.14)
print(zb3)

#zb3.remove(3.14)
zb3.discard(3.14)

zb3.clear()