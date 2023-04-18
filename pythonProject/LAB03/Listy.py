"""
Lab03 - listy
"""

# Tworzenie listy
lista1 = []
print(lista1)

lista1 = [1]
print(lista1)

lista1 = [1, "PJATK", 3.14]
print(lista1)

lista2 = [1, 2, 3]
print(lista2)

napis = "abcdefghijk"
print(list(napis))

lista3: list[int] = [1, 2, 3, 4]

# Indeksowanie list
print(lista3[0])

print(lista3[-1])

print(lista3[0:2])

print(lista3[:2])

# print(lista1[0])#wyswietla perwszy elementy
# print(lista1[-1]) #wyswietla ostatni element
# print(lista1[:2]) #wyswietla perwszy elementy
# print(lista1[1:]) #from begining to the end
# print(lista4[::2])#left every second symbol
# print(lista4[0:-1:2])#left every second symbol
# print(lista4[0:len(lista4):2])#from zero to chosen place

listaA = list(napis)
print(listaA[:-1:2])
print(listaA[:len(listaA) - 1:2])
print(listaA[::-1])

matrix = [1, 2, [3, 4]]
print(matrix[2][0])

# Modyfikowanie listy
lista4 = []
print(lista4)

lista4 = [1]

lista4.append("Lab03") #add in the end something to list
print(lista3)

lista5 = ["1", "2", "3"]
print(lista5)

lista5.insert(1, 3.14) #add in the place you want(1 in the begining is place where you will put something,second value is what you will add)
print(lista5)

lista3.append("3.14")
print(lista3)

lista3.remove("3.14") #remove some text
print(lista3)

lista5.pop()
print(lista5)

lista5.pop(1)
print(lista5)

lista34 = lista3 + lista4
print(lista34)

lista6 = lista4 + [1, 2, 3]

lista5.extend(lista2)
print(lista5)

lista1.append(lista2)
print(lista1)

lista4 = lista4 * 3
print(lista4)

lista3.sort(reverse=False)
print(lista3)

lista3.reverse()
print(lista3)