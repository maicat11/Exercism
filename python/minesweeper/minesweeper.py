def is_mine(grid, i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) and grid[i][j] == '*'


def mine_counter(grid, row, col):
    counter = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if is_mine(grid, i, j):
                counter += 1
    return counter


def board(input_board_array):
    if not input_board_array:
        return input_board_array
    output = []
    row_length = len(input_board_array[0])
    for row in range(len(input_board_array)):
        if len(input_board_array[row]) != row_length:
            raise ValueError('Row length mismatch.')
        line_output = ''
        for col in range(len(input_board_array[row])):
            if input_board_array[row][col] == '*':
                line_output += '*'
            elif input_board_array[row][col] == ' ':
                count = mine_counter(input_board_array, row, col)
                if count == 0:
                    line_output += ' '
                else:
                    line_output += str(count)
            else:
                raise ValueError('Invalid character.')
        output.append(line_output)
    return output