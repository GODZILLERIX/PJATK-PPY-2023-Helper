# #zad1
a = float(input("value a: "))
b = float(input("value b: "))
c = float(input("value c: "))
#dyskryminujący
delta = b**2 - 4 * a * c

if delta > 0:
    print("Dyskryminujący jest większa niż 0.")
else:
    print("Dyskryminujący nie jest większa niż 0.")


# #zad2
word1 = input("Napisz word1: ")
word2 = input("Napisz word2: ")

samogłoski = 'AEIOUaeiou'
word1_new = ''.join(['7' if x in samogłoski else x for x in word1])

spółgłoski  = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
word2_new = ''.join(['6' if x not in samogłoski and x in spółgłoski  else x for x in word2])

result = (word1_new + word2_new).upper()
print(result)

#zad3

bin = input("Podaj liczbę w systemie dwójkowym:bin=")
ósem = input("Podaj liczbę w systemie ósemkowym:oct=")
szesnast = input("Podaj liczbę w systemie szesnastkowym:hex=")

print("Wyniki")
print(f"Zmienna bin zawiera liczbę {bin} zapisaną w systemie dwójkowym, a po konwersji na system dziesiętny jej wartość wynosi {int(bin, 2)}.")
print(f"Zmienna oct zawiera liczbę {ósem} zapisaną w systemie ósemkowym, a po konwersji na system dziesiętny jej wartość wynosi {int(ósem, 8)}.")
print(f"Zmienna hex zawiera liczbę {szesnast} zapisaną w systemie szesnastkowym, a po konwersji na system dziesiętny jej wartość wynosi {int(szesnast, 16)}.")
