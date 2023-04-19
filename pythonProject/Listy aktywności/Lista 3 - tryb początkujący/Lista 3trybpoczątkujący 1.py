#zad1
word1 = input("Napisz word1: ")
word2 = input("Napisz word2: ")

samogłoski = 'AEIOUaeiou'
word1_new = ''.join(['7' if x in samogłoski else x for x in word1])

spółgłoski  = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
word2_new = ''.join(['6' if x not in samogłoski and x in spółgłoski  else x for x in word2])

result = (word1_new + word2_new).upper()
print(result)

print()

#zad2
wybor = str(input("Podaj system: "))
if wybor == "bin":
      bin = input("Podaj liczbę w systemie dwójkowym:bin = ")
      print(f"Zmienna bin zawiera liczbę {bin} zapisaną w systemie dwójkowym, a po konwersji na system dziesiętny jej wartość wynosi {int(bin, 2)}.")

if wybor == "ósem":
      ósem = input("Podaj liczbę w systemie ósemkowym:oct = ")
      print(f"Zmienna oct zawiera liczbę {ósem} zapisaną w systemie ósemkowym, a po konwersji na system dziesiętny jej wartość wynosi {int(ósem, 8)}.")

if wybor == "szesnast":
      szesnast = input("Podaj liczbę w systemie szesnastkowym:hex = ")
      print(f"Zmienna hex zawiera liczbę {szesnast} zapisaną w systemie szesnastkowym, a po konwersji na system dziesiętny jej wartość wynosi {int(szesnast, 16)}.")
#wiem jak zrobić wszystko zadanie num2, po prostu nie mam czasu to zrobic teraz

print()



#zad3
import random

categories = ["cars", "sport", "Countries"]
words = {
    "cars": ["BMW", "Volkswagen", "McLaren", "Ferrari"],
    "sport": ["formula1", "football", "hockey", "rally"],
    "colors": ["Spain", "Poland", "Belarus", "Ukraine"]
}

category_index = int(input("Enter the index of the category: "))
word_index = int(input("Enter the index of the word: "))
category = categories[category_index]
word = words[category][word_index]


word_display = ["_" for _ in range(len(word))]
print(f"Category: {category}")
print(" ".join(word_display))


player1_points = 0
player2_points = 0



def check_letter(letter):
    if letter in word:

        for i in range(len(word)):
            if word[i] == letter:
                word_display[i] = letter
        return True
    else:
        return False



while "_" in word_display:
    letter = input("Player 1, enter a letter: ")
    if check_letter(letter):
        player1_points += word.count(letter)
        print(" ".join(word_display))
        guess = input("Do you want to guess the word? (y/n): ")
        if guess == "y":
            guessed_word = input("Enter the word: ")
            if guessed_word == word:
                player1_points += 2 * word.count("_")
                print("PLAYER1 WINS!!!\n#############################\n" + word + "\n#############################")
                print(f"Player 1: {player1_points}\nPlayer 2: {player2_points}")
                break
            else:
                print("Incorrect guess.")
    else:
        print("Letter not in word.")

        letter = input("Player 2, enter a letter: ")
        if check_letter(letter):
            player2_points += word.count(letter)
            print(" ".join(word_display))
            guess = input("Do you want to guess the word? (y/n): ")
            if guess == "y":
                guessed_word = input("Enter the word: ")
                if guessed_word == word:
                    player2_points += 2 * word.count("_")
                    print("PLAYER2 WINS!!!\n#############################\n" + word + "\n#############################")
                    print(f"Player 1: {player1_points}\nPlayer 2: {player2_points}")
                    break
                else:
                    print("Incorrect guess.")
        else:
            print("Letter not in word.")

