# Zadanie 4 - 10 ptk
# ---------------------------------------------------------------------------------
# Napisz  skrypt,  który  będzie  generował  token uwierzytelniający własnego  autorstwa.
# Użytkownik  po  podaniu  imienia,  nazwiska, adresu  e-mail oraz daty  ważności  tokena powinien otrzymać unikalny token.
# Skrypt powinien również umożliwić wprowadzenie tokena  i  sprawdzenie  jego  ważności.  Na  postawie  tokena powinniśmy uzyskać dane użytkownika.

import datetime
import random

users_data = {}

def generate_token(first_name, last_name, email, valid_until):
    # Generate a random token using a combination of letters and digits
    token = ''.join(chr(ord('a') + random.randint(0, 25)) for _ in range(10))
    users_data[token] = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'valid_until': valid_until,
    }
    return token

def check_token_validity(token):
    if token in users_data:
        valid_until = users_data[token]['valid_until']
        if valid_until >= datetime.datetime.now():
            return True
    return False

def get_user_data(token):
    if token in users_data:
        return users_data[token]
    return None

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email address: ")
valid_until_str = input("Enter the token validity date (YYYY-MM-DD): ")

valid_until = datetime.datetime.strptime(valid_until_str, "%Y-%m-%d")

token = generate_token(first_name, last_name, email, valid_until)
print("Generated token:", token)

input_token = input("Enter the token to check: ")
if check_token_validity(input_token):
    user_data = get_user_data(input_token)
    print("User Data:")
    print("First Name:", user_data['first_name'])
    print("Last Name:", user_data['last_name'])
    print("Email:", user_data['email'])
    print("Token Validity:", user_data['valid_until'])
else:
    print("Invalid token or token has expired.")
