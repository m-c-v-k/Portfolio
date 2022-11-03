#! python3
### table_printer.py ###
### Takes a list containing other lists and prints it neatly and right justified ###

table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def print_table(table_data):
    """ Takes a list containing other lists and prints it neatly and right justified

    Args:
        table_data (List): A List containing other lists.
    """

    column_width = [0] * len(table_data)

    for i, column_data in enumerate(table_data):

        for row_item in column_data:
            item_length = len(row_item)

            if item_length > column_width[i]:
                column_width[i] = item_length

    num_columns = len(table_data)
    num_rows = len(table_data[0])

    for row_index in range(num_rows):

        for column_index in range(num_columns):
            print(table_data[column_index][row_index].rjust(
                column_width[column_index]), end=' ')
        print('')


print_table(table_data)
