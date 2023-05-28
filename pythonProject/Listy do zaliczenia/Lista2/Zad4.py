# Zadanie 4 - 10 ptk
# ---------------------------------------------------------------------------------
# Napisz  skrypt,  który  będzie  generował  token uwierzytelniający własnego  autorstwa.
# Użytkownik  po  podaniu  imienia,  nazwiska, adresu  e-mail oraz daty  ważności  tokena powinien otrzymać unikalny token.
# Skrypt powinien również umożliwić wprowadzenie tokena  i  sprawdzenie  jego  ważności.  Na  postawie  tokena powinniśmy uzyskać dane użytkownika.

user_data = {}

def generate_unique_number():

    if len(user_data) == 0:
        return 1
    else:
        return max(user_data.keys()) + 1

def add_user():

    first_name = input("Podaj imię użytkownika: ")
    last_name = input("Podaj nazwisko użytkownika: ")
    email = input("Podaj adres e-mail użytkownika: ")
    date = input("Podaj datę użytkownika (w formacie DD.MM.RRRR): ")

    unique_number = generate_unique_number()
    user_data[unique_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'date': date
    }
    print()
    print(f"Użytkownik o unikalnym numerze {unique_number} został dodany.")
    print()

def find_user():

    unique_number = int(input("Podaj unikalny numer użytkownika: "))

    if unique_number in user_data:
        user = user_data[unique_number]
        print(f"Imię: {user['first_name']}")
        print(f"Nazwisko: {user['last_name']}")
        print(f"Adres e-mail: {user['email']}")
        print(f"Data: {user['date']}")
    else:
        print()
        print("Nie znaleziono użytkownika o podanym unikalnym numerze.")
        print()

def main():
    while True:
        print()
        print("Wybierz akcję:")
        print("1. Dodaj użytkownika")
        print("2. Znajdź użytkownika po unikalnym numerze")
        print("3. Wyjdź")
        print()

        choice = input("Podaj numer akcji: ")
        print()

        if choice == '1':
            add_user()
        elif choice == '2':
            find_user()
        elif choice == '3':
            break
        else:
            print("Nieprawidłowe dane wejściowe. Spróbuj ponownie.")

if __name__ == '__main__':
    main()
