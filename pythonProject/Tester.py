# Code to take input of a list
# from the user.

# Take input of the size of the list
n = int (input ("Podaj wartość k: "))

# Declare an empty list
list = []

# Iterate for n times take inputs
for i in range (n):
    # Take input of ith element as x.
    x = int(input())
    # Append 'x' to the list.
    list.append(x)

# Print the list
print("List:", list)


a = int(input("Podaj początek zakresu: "))
b = int(input("Podaj koniec zakresu: "))
#k = int(input("Podaj wartość k: "))
n = int (input ("Podaj wartość k: "))

list = []
res = {}
for i in range (n):
    # Take input of ith element as x.
    x = int(input())
    # Append 'x' to the list.
    list.append(x)

for i in range(a, b+1):
    if i % k == 0:
        if k not in res:
            res[k] = []
        res[k].append(i)

print(res)
