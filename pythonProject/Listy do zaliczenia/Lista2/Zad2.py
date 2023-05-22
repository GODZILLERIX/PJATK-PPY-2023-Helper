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
def pkwadrat(num1):
    return num1 ** 0.5
def pierwiastek_dowolnego_stopnia(num1, num2):
    return num1 ** (1 / num2)
def potęga(num1, num2):
    return num1 ** num2

x = input("Enter an operator (+, -, *, /, //, %, pkwdrt, pds, pot): ")


if x == "+":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result1 = dodawanie(num1, num2)
    print(result1)

elif x == "-":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result2 = odejmowanie(num1, num2)
    print(result2)

elif x == "*":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result3 = mnożenie(num1, num2)
    print(result3)

elif x == "/":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result4 = dzielenie(num1, num2)
    print(result4)

elif x == "//":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result5 = dzielenia_bez_reszty(num1, num2)
    print(result5)

elif x == "%":
    num1 = float(input("Enter procents: "))
    num2 = float(input("Enter the number: "))
    result6 = procent(num1, num2)
    print(result6)

elif x == "pkwdrt":
    num1 = float(input("Enter the number: "))
    result7 = pkwadrat(num1)
    print(result7)

elif x == "pds":
    num1 = float(input("Enter the number: "))
    num2 = float(input("Enter degree: "))
    result8 = pierwiastek_dowolnego_stopnia(num1, num2)
    print(result8)

elif x == "pot":
    num1 = float(input("Enter the number: "))
    num2 = float(input("Enter degree: "))
    result9 = potęga(num1, num2)
    print(result9)
