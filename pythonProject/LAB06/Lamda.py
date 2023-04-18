"""
Wyrażenia lambda
"""

l = lambda a, b, c: a + b + c
print(l(2, 3, 4))

lista = [(lambda a: a * 2), (lambda a: a * 4), (lambda a: a * 6)]

for el in lista:
    print(el(2))

print(lista[1](3))
