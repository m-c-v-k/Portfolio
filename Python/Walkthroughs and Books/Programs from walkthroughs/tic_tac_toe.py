#! python3

### A complete Tic-Tac-Toe game ###
### Made using http://inventwithpython.com/chapter10.html as guide ###

import random


def draw_board(board):
    """ This function prints out the board as it is passed.

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.
    """

    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')


def input_player_letter():
    """ This function lets the player decide if they want to be X or O.

    Returns:
        List: Player's letter as the first list item, and the computer's letter
        as the second list item.
    """

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    """ This function decides if the computer or the player will start playing.
        This is done using the random module.

    Returns:
        String: A string saying if the computer or the player starts playing.
    """

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    """ This function returns True if the player choses to play again, else False.

    Returns:
        Boolean: True if the input starts with 'y'.
                 False if the input does not start with 'y'.
    """

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    """ This function assigne the moves on the board to the current player.

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.
        letter (String): The string X or O, depending on the turn to be inserted
            on move.
        move (String): String deciding where the letter should be placed in the
            board list.
    """

    board[move] = letter


def is_winner(board, letter):
    """ This function checks if the current player wins with its move.

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.
        letter (String): The string X or O, depending on the turn to be inserted
            on move.

    Return:
        Boolean: True if there's three-in-a-row.
                 False if there's no three-in-a-row.
    """

    return(
        # Horizontal-top
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        # Horizontal-mid
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        # Horizontal-low
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        # Vertical-left
        (board[7] == letter and board[4] == letter and board[1] == letter) or
        # Vertical-mid
        (board[8] == letter and board[5] == letter and board[2] == letter) or
        # Vertical-right
        (board[9] == letter and board[6] == letter and board[3] == letter) or
        # Diagonal
        (board[7] == letter and board[5] == letter and board[3] == letter) or
        # Diagonal
        (board[9] == letter and board[5] == letter and board[1] == letter)
    )


def copy_board(board):
    """ This function duplicates the board

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.

    Return:
        List: A duplicate of the board list.
    """

    board_copy = []

    for i in board:
        board_copy.append(i)

    return board_copy


def is_space_free(board, move):
    """ This function checks if the move is on a non-occupied spot

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.
        move (string): String deciding where the letter should be placed in the
            board list.

    Return:
        Boolean: True if the move is to ' ' on the board.
                 False if move is to any other character on the board.
    """

    return board[move] == ' '


def get_player_move(board):
    """ This function let's the player chose a move.

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.

    Return:
        Int: Integer 1-9 on the player's move.
    """

    move = ''

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()

    return int(move)


def chose_random_move_from_list(board, moves_list):
    """_summary_

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.
        moves_list (List): A list of possible moves

    Return:
        List: If conditions are met, and there are possible moves.
        None: If conditions are not met, and there are no possible moves.
    """
    possible_moves = []

    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    """ This function decides on the computer's move.
        The decition is based on order of urgency, giving the computer
        a sense of 'AI'.

    Args:
        board (List): The board consists of a list of 10 strings,
            ignoring index 0.
        computer_letter (String): 'X' or 'O', depending on what the player
            chose when starting the game.

    Returns:
        Int: Integer 1-9 on the computer's move.
    """

    # Used to determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Check if it's possible to win in the next move.
    for i in range(1, 10):
        copy = copy_board(board)

        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)

            if is_winner(copy, computer_letter):
                return i

    # Check if the player could win in the next move.
    for i in range(1, 10):
        copy = copy_board(board)

        if is_space_free(copy, i):
            make_move(copy, player_letter, i)

            if is_winner(copy, player_letter):
                return i

    # Try to take possible free corner.
    move = chose_random_move_from_list(board, [1, 3, 7, 9])

    if move != None:
        return move

    # Try to take center.
    if is_space_free(board, 5):
        return 5

    # Move on the sides.
    return chose_random_move_from_list(board, [8, 4, 6, 2])


def is_board_full(board):
    """ This function checks if the board is full or not.

    Args:
        board (list): The board consists of a list of 10 strings,
            ignoring index 0.

    Returns:
        Boolean: True if every value is taken.
                 False if any value is not taken.
    """

    for i in range(1, 10):
        if is_space_free(board, i):
            return False

    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Main loop, running the whole game.

    # Reset the board.
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()

    print('The ' + turn + ' will go first.')

    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Congratulations! You won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
