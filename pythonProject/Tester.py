# words = []
#
# for i in range(1):
#     word = input("Podaj słowo: ")
#     words.append(word)
#
# print("Lista słów:", words)

# import random

# def print_random_order(data_list):
#     random.shuffle(data_list)
#     for item in data_list:
#         print(item)
#
# data_list = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango']
#
# print("Dane w losowej kolejności:")
# print_random_order(data_list)


# def data(word1, word2, word3, word4):
#     new_word = ""
#     words = [word1, word2, word3, word4]
#     for word in words:
#         if len(word) > 0:
#             new_word += word[0].upper()
#     return new_word
#
# word1 = input("Podaj imię: ")
# word2 = input("Podaj nazwisko: ")
# word3 = input("Podaj E-mail: ")
# word4 = input("Podaj data ważności: ")
#
# data = data(word1, word2, word3, word4)
# print("Wygenerowane słowo:", data)

user_data = {}  # Словарь для хранения данных пользователей

def generate_unique_number():
    """
    Генерирует уникальный номер пользователя
    """
    if len(user_data) == 0:
        return 1
    else:
        return max(user_data.keys()) + 1

def add_user():
    """
    Запрашивает у пользователя имя, фамилию и адрес электронной почты,
    и добавляет информацию о пользователе в словарь user_data
    """
    first_name = input("Введите имя пользователя: ")
    last_name = input("Введите фамилию пользователя: ")
    email = input("Введите адрес электронной почты пользователя: ")

    unique_number = generate_unique_number()
    user_data[unique_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    print()

    print(f"Пользователь с уникальным номером {unique_number} добавлен.")
    print()

def find_user():
    """
    Запрашивает у пользователя уникальный номер и выводит информацию о пользователе
    """
    unique_number = int(input("Введите уникальный номер пользователя: "))

    if unique_number in user_data:
        user = user_data[unique_number]
        print()
        print(f"Имя: {user['first_name']}")
        print(f"Фамилия: {user['last_name']}")
        print(f"Адрес электронной почты: {user['email']}")
    else:
        print()
        print("Пользователь с указанным уникальным номером не найден.")
        print()

def main():
    while True:
        print()
        print("Выберите действие:")
        print("1. Добавить пользователя")
        print("2. Найти пользователя по уникальному номеру")
        print("3. Выйти")
        print()

        choice = input("Введите номер действия: ")
        print()

        if choice == '1':
            add_user()
        elif choice == '2':
            find_user()
        elif choice == '3':
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

if __name__ == '__main__':
    main()
