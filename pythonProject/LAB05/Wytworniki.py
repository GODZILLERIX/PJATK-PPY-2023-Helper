"""
Lab05 - wytworniki
"""

l = range(1, 21, 2)
print(list(l))

# postac prosta

# lista składana
l1 = [a * 5 for a in (1, 2, 3)]
print(l1)

# lista krotek
k1 = [(a, a + 1) for a in (1, 2, 3)]
print(k1)

# słownik składany
s1 = {a: a + 1 for a in [1, 2, 3]}
print(s1)

# podwajanie wartości
print([2 * x for x in l])

# para (x, kawadrat x)
print([(x, x * x) for x in range(1, 5)])

# tabela kodowa ASCII
print([(x, ord(x)) for x in "ABCDEF"])

# lista zawierjaca 10 pustych list
print([[] for x in range(10)])

# postać prosta warunkowa

# liczby wieksze od 10
print([x for x in l if x > 10])

# liczby podzielne przez 3 lub 5
print([x for x in range(1, 20) if not (x % 3) or not (x % 5)])

# tabela kodowa ASCII dla samogłosek
print([(x, ord(x)) for x in "ABCDEF" if x in "AEIOUY"])

# postac rozszerzona

# pary każdy element z kazdym
print([(x, y) for x in range(1, 5)
       for y in range(4, 0, -1)])

# róznica miedzy wartoscia z pierwszej i drugiej listy
print([x - y for x in range(1, 5)
       for y in range(4, 0, -1)])

# sklejenie napisu z wartosci pochodzacych z trzech list
print([str(x) + y + str(z) for x in [1, 2]
       for y in ["A", "B"]
       for z in [0, 3]])

# postac rozszerzona z jednym warunkiem

# para kazdy element z kadym tylko jezeli pierwszy
# element jest mniejszy od drugiego
print([(x, y) for x in range(1, 5)
       for y in range(6, 3, -1)
       if x < y])

# para kazdy element z kazdym tylko jezeli
# suma elementow jest mniejsza od 7
print([(x, y) for x in range(1, 5)
       for y in range(6, 3, -1)
       if x + y < 7])

# para kazdy element z kazdym pod warunkiem ze
# pierwzy element jest parzysty lub drugi jest
# nieparzysty
print([(x, y) for x in range(1, 5)
       for y in range(6, 2, -1)
       if not (x % 2) or y % 2])

# postać rozszerzona z wieloma warunkami

# para kazdy element z kazdym pod warunkiem ze
# pierwszy elemnt jest parzysty
# a drugi jest nieparzysty
print([(x, y) for x in range(1, 5) if not (x % 2)
       for y in range(6, 2, -1) if y % 2])
