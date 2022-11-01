#! Python3

# Project 8 - Part 2 - Tic Tac Toe
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


def player_move(icon):

    # Announce who's turn it is
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print(f"Your turn player {number}.")

    # Ask for the player's move
    choice = int(input("Please enter your move (1-9): ").strip())

    # Check if choice is free
    if board[choice - 1] == " ":

        # Place user move on board
        board[choice - 1] = icon

    else:
        print()
        print("That place is already taken.")


def is_victory(icon):

    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():

    # Check if board is full
    if " " not in board:
        return True
    else:
        return False


    # Game control loop
while True:

    # Print the game board
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
