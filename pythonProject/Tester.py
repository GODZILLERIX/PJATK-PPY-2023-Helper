a = int(input("Podaj początek zakresu: "))
b = int(input("Podaj koniec zakresu: "))
n = int(input("Podaj długość lista wartośćiej k: "))

list = []
for i in range(n):
    element = int(input("Podaj wartośći k: "))
    list.append(element)

    for element in list:
        res = {}
        for i in range(a, b+1):
            if i % element == 0:
                if element not in res:
                    res[element] = []
                res[element].append(i)

        print(res)

        # print(element)


# res = {}
# for i in range(a, b+1):
#     if i % k == 0:
#         if k not in res:
#             res[k] = []
#         res[k].append(i)

# print(res)
#
# n = int(input("Enter the length of the list: "))
# list = []
#
# for i in range(n):
#     element = int(input("Enter element: "))
#     list.append(element)
#
# print(list)


# lst = [1, 2, 3, 4, 5]
# for element in lst:
#     print(element)
