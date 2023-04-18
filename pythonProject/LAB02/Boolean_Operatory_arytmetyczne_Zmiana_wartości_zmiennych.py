"""
Typ logiczny Boolean, operatory arytmetyczne,
zmiana wartości zmiennych
"""

a = True
b = False
print(a, b)

# operatory wyrażeń Boolean
x = 2
y = 4

print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)

print(a or b)
print(a and b)
print(not a)
print(not b)

# Operatory arytmetyczne
a, b = 2, 3

print(a + b)  # dodawanie
print(a - b)  # odejmowanie
print(a * b)  # mnozenie
print(a / b)  # dzielenie
print(a % b)  # reszta z dzielenia
print(a ** b)  # potega

# Zmiana wartosci zmiennych

a, b, c, d, e = 1, 3, 7, 4, 6
a += 2
b -= 2
c *= 2
d /= 2
print(a, b, c, d, e)
