"""
Lab04 - petla while
"""

# przyklad prostej petli while
x = 0
while x < 10:
    x += 1
    print(x)

print()

x = {1, 2, 3, 4, 5}
while x:
    print(x.pop())
else:
    print("Zbiór x jest pusty")

print()

# przykład zagnieżdzonej pętli while
x = 0
while x < 10:
    x += 1
    print(x)
    a = 1
    while a < 5:
        a *= 2
        print("a=" + str(a))
s