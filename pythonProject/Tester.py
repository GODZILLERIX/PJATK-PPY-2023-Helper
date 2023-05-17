# #Zadanie 1 - 4 ptk
# # ---------------------------------------------------------------------------------
# #Napisz skrypt, który pobierze od użytkownika 3 liczby całkowite i w odpowiedzi na
# #ekranie wyświetli liczbę gwizdek, # i $ np.:
# #   * # $
# #   * # $
# #   * #
# #   *
# #   *
# #Każdy znak to osobna kolumna. Zastosuje odpowiednie formatowanie
#
# def zad1():
#     a = int(input("Podaj pierwszą liczbę: "))
#     b = int(input("Podaj drugą liczbę: "))
#     c = int(input("Podaj trzecią liczbę: "))
#
#     for i in range(max(a, b, c)):
#
#         if i < a:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#
#         if i < b:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#
#         if i < c:
#             print("$", end="")
#         else:
#             print(" ", end="")
#
#         print()
# zad1()

print()

#Zadanie 2 - 6 ptk
# ---------------------------------------------------------------------------------
#Napisz skrypt, który będzie działał jak prosty kalkulator (obsługa dodawania,
#odejmowania, mnożenia, dzielenia, dzielenia bez reszty, %, pierwiastek kwadratowy,
#pierwiastek dowolnego stopnia, potęga)





def dodawanie(num1, num2):
    return num1 + num2
def odejmowanie(num1, num2):
    return num1 - num2
def mnożenie(num1, num2):
    return num1 * num2
def dzielenie(num1, num2):
    return num1 / num2
def dzielenia_bez_reszty(num1, num2):
    return num1 // num2
def procent(num1, num2):
    return (num1 / 100) * num2
def pkwadrat(num1, num2):
    return num1 + num2
def pierwiastek_dowolnego_stopnia(num1, num2):
    return num1 + num2
def potęga(num1, num2):
    return num1 + num2

x = input("Enter an operator (+, -, *, /, //, %, pkwdrt): ")


if x == "+":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result1 = dodawanie(num1, num2)
    print(result1)

# elif x == "-":
#     result2 = num1 - num2
#     print(result2)
#
# elif x == "*":
#      result3 = num1 * num2
#      print(result3)
#
# elif x == "/":
#     result4 = num1 / num2
#     print(result4)
#
# elif x == "//":
#     result5 = num1 // num2
#     print(result5)
#
# elif x == "%":
#     result6 = (num1 / 100) * num2
#     print(result6)





# def kwadrat():
#
#     if x == "kwdrt":
#         kwadrat()
#         num3 = float(input("Enter the number"))
#         result7 = num3 ** (0.5)
#         print(result7)
#
# #elif x ==
# numbers()
# kwadrat()


# x = input("Enter an operator (+, -, *, /, //, %, pkwdrt): ")
#
#
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if x == "+":
#     result1 = num1 + num2
#     print(result1)
#
# elif x == "-":
#     result2 = num1 - num2
#     print(result2)
#
# elif x == "*":
#     result3 = num1 * num2
#     print(result3)
#
# elif x == "/":
#     result4 = num1 / num2
#     print(result4)
#
# elif x == "//":
#     result5 = num1 // num2
#     print(result5)
#
# elif x == "%":
#     result6 = (num1 / 100) * num2
#     print(result6)
#
#     if x == "kwdrt":
#         num3 = float(input("Enter the number"))
#         result7 = num1 ** (0.5)
#         print(result7)
#
# #elif x ==
#
#
# else:
#     print(f"{x} is not a valid operator")
