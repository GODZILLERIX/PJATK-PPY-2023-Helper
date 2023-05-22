#Zadanie 1 - 4 ptk
# ---------------------------------------------------------------------------------
#Napisz skrypt, który pobierze od użytkownika 3 liczby całkowite i w odpowiedzi na
#ekranie wyświetli liczbę gwizdek, # i $ np.:
#   * # $
#   * # $
#   * #
#   *
#   *
#Każdy znak to osobna kolumna. Zastosuje odpowiednie formatowanie

def zad1():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = int(input("Podaj trzecią liczbę: "))

    for i in range(max(a, b, c)):

        if i < a:
            print("*", end=" ")
        else:
            print(" ", end=" ")

        if i < b:
            print("#", end=" ")
        else:
            print(" ", end=" ")

        if i < c:
            print("$", end="")
        else:
            print(" ", end="")

        print()
zad1()