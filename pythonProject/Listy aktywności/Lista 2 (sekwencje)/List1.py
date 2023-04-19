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

#-------------------------------------------------------------------------------------------


#zad2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def raise_to_power_of_2(num):
    if num % 2 == 0:
        return num**2
    return num

numbers = []
for i in range(20):
    num = int(input("•Enter a number between -20 and 20: "))
    while num < -20 or num > 20:
        num = int(input("Invalid number. Enter a number between -20 and 20: "))
    numbers.append(num)

print("Original List:", numbers)

copy_list = numbers.copy()

prime_numbers = tuple(filter(is_prime, copy_list))
print("Prime Numbers Tuple:", prime_numbers)

power_of_2_numbers = tuple(map(raise_to_power_of_2, copy_list))
print("Power of 2 Numbers Tuple:", power_of_2_numbers)

for i, num in enumerate(numbers):
    if num % 2 == 0:
        numbers[i] = 'A'
print("Updated Original List:", numbers)

#-------------------------------------------------------------------------------------------


#zad3
size = int(input("•Enter the size of multiplication table: "))

numbers = list(range(1, size+1))

table = [[str(i*j) for j in numbers] for i in numbers]

max_len = len(str(size*size))

for row in table:
    print(" ".join(num.rjust(max_len) for num in row))


#-------------------------------------------------------------------------------------------


#zad4
def catalan(n):
    """
    This function calculates the nth Catalan number recursively.
    """
    if n == 0:
        return 1
    else:
        return ((4*n - 2) * catalan(n-1)) // (n+1)

limit = int(input("Enter a limit for Catalan numbers: "))

n = 0
while catalan(n) < limit:
    print(catalan(n))
    n += 1


#-------------------------------------------------------------------------------------------


#zad5

products = {}

def add_product():

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    # Find the next available product number
    num = max(products.keys(), default=0) + 1
    products[num] = {"name": name, "quantity": quantity, "price": price}
    print("Product added successfully.")

def delete_product():

    num = int(input("Enter product number to delete: "))
    if num in products:
        del products[num]
        print("Product deleted successfully.")
    else:
        print("Product not found.")

def display_products():

    print("No\tProduct name\tQuantity\tPrice")
    for num, data in products.items():
        print(f"{num}\t{data['name']}\t\t{data['quantity']}\t\t{data['price']}")

def modify_product():

    num = int(input("Enter product number to modify: "))
    if num in products:
        data = products[num]
        name = input(f"Enter new name ({data['name']}): ")
        quantity = input(f"Enter new quantity ({data['quantity']}): ")
        price = input(f"Enter new price ({data['price']}): ")
        if name:
            data['name'] = name
        if quantity:
            data['quantity'] = int(quantity)
        if price:
            data['price'] = float(price)
        print("Product modified successfully.")
    else:
        print("Product not found.")

while True:
    print("\nChoose an option:")
    print("1. Add product")
    print("2. Delete product")
    print("3. Display products")
    print("4. Modify product")
    print("5. Quit")
    choice = input("> ")
    if choice == "1":
        add_product()
    elif choice == "2":
        delete_product()
    elif choice == "3":
        display_products()
    elif choice == "4":
        modify_product()
    elif choice == "5":
        break
    else:
        print("Invalid option. Try again.")










