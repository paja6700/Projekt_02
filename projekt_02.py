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

