"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: Pavel Křivan
email: paja6700@gmail.com
discord: pavel007111
"""

import sys

#show game rules
def show_rules():
    print("""Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game""")
    
#show game board
def display_board(board):
    print("========================================")
    for row in board:
        print("+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+")
    print("========================================")

#check a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != " ":
            return board[0][column]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

#draw check, if the board is full
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

#main game function
def main():
    show_rules()

    #initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["O", "X"]
    current_player = 0

    while True:
        display_board(board)
        print(f"Player {players[current_player]} | Please enter your move number: ")

        try:
            move = int(input()) - 1
            if move < 0 or move >= 9:
                print("Wrong move. Choose a number between 1 and 9.")
                continue

            row, column = divmod(move, 3)
            if board[row][column] != " ":
                print("Wrong move. Place is already occupied.")
                continue

            #place the player's mark
            board[row][column] = players[current_player]

            #check a winner
            winner = check_winner(board)
            if winner:
                display_board(board)
                print(f"Congratulations, the player {winner} WON!")
                break

            #draw check
            if is_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            #switch player
            current_player = 1 - current_player

        except ValueError:
            print("Wrong input. Enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
