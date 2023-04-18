"""
Lab04 - petla for
"""

# Przykłady petli for
listaA = ["abc", [1, 2, 3]]

for i in listaA:
    print(i)

print()

for i in range(len(listaA)):
    print(i)

print()

for i in listaA:
    print(i)
    for j in i:
        print(j)

print()

# Przyklady formatowania tesktu (python 2.7 i python 3.x)
for x in range(-10, 11):
    print("%+i" % x, end=" ")  # + - znak przed liczbą

print("\n")

for x in range(5, 100, 10):
    print("%3i%6o%5x" % (x, x, x))  # wyrowanie od prawej

print()

for x in range(5, 100, 10):
    print("%#-3i%#-6o%#-5x" % (x, x, x))  # wyrowanie od lewej (# - wlasciwy prefix)

print()

for x in range(5, 100, 10):
    print("%03i %04o %04x" % (x, x, x))

print()

# formatowanie dla python 3.x
for x in range(5, 100, 10):
    print("{} {} {}".format(x, oct(x), hex(x)))