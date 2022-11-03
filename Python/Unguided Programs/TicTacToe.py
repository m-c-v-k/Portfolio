#! Python3

# A simple Tic Tac Toe game

# Importing necessary libraries
import random


def player_move(player):
    """player move Handles the players moves on the game board

    Args:
        player (string): 'X' or 'O' depending on what the player chose.
    """

    while True:
        try:
            move = int(input("Please enter your move (1-9): "))
            move -= 1
            try:
                if is_valid(move) == True or "Exit":
                    break
            except:
                print("Your move was invalid, please enter a new one.")
        except:
            print("You must enter an integer between 1 and 9")

    board[move] = player


# TODO Improve computer moves


def computer_move(player):
    '''computer_move Handles the computers moves on the game board

    Args:
        player (string): 'X' or 'O' depending on what the player chose.
    '''

    while True:
        try:
            move = random.randint(0, 8)
            if is_valid(move) == True:
                break
        except:
            print("Your move was invalid, please enter a new one.")

    board[move] = player2
    print("The computer made its move.")


def is_valid(move):
    '''is_valid Checks if the move is valid

    Args:
        move (int): Integer representing the placement on the game board

    Returns:
        bool: Returns True or False depending if move is valid or not
    '''

    if board[move] == " ":
        move_valid = True
    else:
        move_valid = False

    return move_valid


def handle_turn():
    '''handle_turn Handles turns and moves
    '''

    global turn

    if number_of_players == 1:
        if turn == 1:
            player_move(player1)
        elif turn == 2:
            computer_move(player2)
    elif number_of_players == 2:
        if turn == 1:
            player_move(player1)
        elif turn == 2:
            player_move(player2)

    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1


def print_board():
    '''print_board Prints out the current game board.
    '''
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |\n")


# Create board
board = []

for x in range(9):
    board.append(" ")

# Select number of players
while True:
    try:
        number_of_players = int(
            input("Please enter 1 or 2 depending on the number of players: "))
        number_of_players == 1 or number_of_players == 2
        break

    except:
        print("Please enter '1' or '2'.")

# Select X or O
while True:
    try:
        player1 = input(
            "Please select if you wish to be 'X' or 'O': ").strip().upper()
        player1 == "X" or player1 == "O"
        break

    except:
        print("Please enter 'X' or 'O'.")


if player1 == "X":
    player2 = "O"
elif player1 == "O":
    player2 = "X"

# Select who starts
first_move = random.randint(1, 2)

if number_of_players == 1:
    if first_move == 1:
        print("The player gets the first move!")
    elif first_move == 2:
        print("The computer gets the first move!")
elif number_of_players == 2:
    if first_move == 1:
        print("Player 1 gets the first move!")
    elif first_move == 2:
        print("Player 2 gets the first move!")

turn = first_move

# Control-loop
while True:

    # Print board
    print_board()

    # Handle Moves
    handle_turn()

    # TODO Check if win
    # TODO Play again or quit
    # TODO Check if draw
