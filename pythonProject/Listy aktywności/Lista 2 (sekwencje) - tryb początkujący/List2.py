#zad1
a = str(input("Imię: "))
b = str(input("Datę urodzenia: "))
c = str(input("Adres e-mail: "))
d = int(input("Numer telefonu: "))

lista1 = [a, b, c, d]
print(lista1)

krotka1 = (a, b, c, d)
print(krotka1)

thisdict = {
  "Imię": a,
  "Datę urodzenia": b,
  "Adres e-mail": c,
  "Numer telefonu": d
}
print(thisdict)
#--------------------------------------------------------------------------------------------------------------------------
#zad2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

my_list = [1, 2, 'three', 4, 5.0, 'six', 7, 8, 9, 'ten', 11, 'twelve', 13, 14, 15, 'sixteen', 17, 18, 19, 'twenty']

for i in range(len(my_list)):
    if is_prime(i):
        print(my_list[i])

#--------------------------------------------------------------------------------------------------------------------------

#zad3
letters = input("Enter a list of uppercase letters: ").split(",")
numbers = input("Enter a list of numbers from 1 to 10: ").split(",")

my_dict = dict(zip(letters, numbers))

print(my_dict)


