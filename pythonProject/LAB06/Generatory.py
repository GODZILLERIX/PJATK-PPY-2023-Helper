"""
Generatory
"""


def generator(a):
    for i in range(a):
        yield i + 1


for i in generator(4):
    print(i, end='')

print('')
gen = generator(5)
print(next(gen))
print(next(gen))
print(next(gen))