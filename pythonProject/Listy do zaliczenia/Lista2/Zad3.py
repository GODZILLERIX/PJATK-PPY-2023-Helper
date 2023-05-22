# Zadanie 3 - 8 ptk
# ---------------------------------------------------------------------------------
# Napisz skrypt, którybędziegrą w kółko i krzyżyk

board = [' '] * 9
current_player = 'X'

def board_create():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

def moves():
    global current_player
    position = int(input("Choose cell(from 1 to 9): ")) - 1
    if board[position] == ' ':
        board[position] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print("Incorrect cell! Try again.")
        moves()

def winner_check():
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return True
    return False

def play_game():
    board_create()
    while not winner_check():
        moves()
        board_create()
        if ' ' not in board:
            break
    if winner_check():
        if current_player == 'X':
            winner = 'O'
        else:
            winner = 'X'
        print(f"Player {winner} won!")
    else:
        print("Draw!")

play_game()