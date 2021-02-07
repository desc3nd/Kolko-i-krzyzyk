from asyncio import sleep

def display_board(board):
    counter = 1
    for row in range(3):
        for col in range(3):
            print("|", board[row][col], " ", end="")
        print()


# Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
# i wyświetla go w oknie konsoli.
#

def enter_move(board):
    move = input("podaj swój ruch")
    while not move.isdigit():
        move = input("podaj swój ruch PAMIETAJ ŻEBY WPISAC LICZBĘ CAŁKOWITĄ NP 1:")
    var = False
    for row in range(3):
        for col in range(3):
            if board[row][col] == int(move):
                board[row][col] = 'O'
                var = True
    if var != True:
        print("to miejsce jest już zajęte! bądź nie należy do zakresu gry")
        enter_move(board)


# Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
# prosi użytkownika o wykonanie ruchu,
# sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
#

def make_list_of_free_fields(board):
    empty = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O' and board[row][col] != 'X':
                tup = (row, col)
                empty.append(tup)
    return empty


# Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól;
# lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.

def victory_for(sign, board):
    if sign != "RUNNING":
        print("ups..coś jest nie tak")
        exit()
    sign = "RUNNING"
    X_O = ('X', 'O')
    for gamer in X_O:
        if board[0][0] == gamer and board[0][1] == gamer and board[0][2] == gamer:  # 1 rzad
            sign = gamer + " wygrywa"
            return sign
        if board[1][0] == gamer and board[1][1] == gamer and board[1][2] == gamer:  # 2 rzad
            sign = gamer + " wygrywa"
            return sign
        if board[2][0] == gamer and board[2][1] == gamer and board[2][2] == gamer:  # 3 rzad
            sign = gamer + " wygrywa"
            return sign
        if board[0][0] == gamer and board[1][1] == gamer and board[2][2] == gamer:  # na ukos od lewa
            sign = gamer + " wygrywa"
            return sign
        if board[0][2] == gamer and board[1][1] == gamer and board[2][0] == gamer:  # na ukos na prawo
            sign = gamer + " wygrywa"
            return sign
        if board[0][0] == gamer and board[1][0] == gamer and board[2][0] == gamer:  # 1 kolumna
            sign = gamer + " wygrywa"
            return sign
        if board[0][1] == gamer and board[1][1] == gamer and board[2][1] == gamer:  # 2 kolumna
            sign = gamer + " wygrywa"
            return sign
        if board[0][2] == gamer and board[1][2] == gamer and board[2][2] == gamer:  # 3 kolumna
            sign = gamer + " wygrywa"
            return sign
    tab = make_list_of_free_fields(board)
    if len(tab) == 0:
        sign = "REMIS"
    return sign


# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
#

def draw_move(board):
    import random
    row = random.randrange(0, 3)
    col = random.randrange(0, 3)
    while board[row][col] == 'O' or board[row][col] == 'X':
        row = random.randrange(0, 3)
        col = random.randrange(0, 3)
    board[row][col] = 'X'


# Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.
#
board = [[0 for i in range(3)] for j in range(3)]
counter = 1
for row in range(3):
    for col in range(3):
        board[row][col] = counter
        counter = counter + 1
board[1][1] = 'X'
sign = "RUNNING"
while sign == "RUNNING":
    display_board(board)
    enter_move(board)
    draw_move(board)
    make_list_of_free_fields(board)
    sign = victory_for(sign, board)
display_board(board)
print(sign)
import time
time.sleep(10)