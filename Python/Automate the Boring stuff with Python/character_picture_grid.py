def character_picture_grid():
    """ Prints a list containing lists rotaded 90 degrees clock-wise.
    """
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if j < len(grid) - 1:
                print(grid[j][i], end="")
            else:
                print(grid[j][i])


character_picture_grid()
