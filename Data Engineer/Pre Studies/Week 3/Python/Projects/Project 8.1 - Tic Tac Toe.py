#! Python3

# Project 8 - Part 1 - Tic Tac Toe
# A small Tic Tac Toe game

# Making the board
board = [" " for i in range(9)]


def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


# Game control loop
while True:

    # Print the game board
    print_board()

    # Ask for the player's move
    choice = int(input("Please enter your move (1-9): ").strip())

    # Check if choice is free
    if board[choice - 1] == " ":

        # Place user move on board
        board[choice - 1] = "X"

    else:
        print()
        print("That place is already taken.")
