import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))


def is_lower_than_neighbours(coords, board):
    print(coords, len(board[0]), len(board))
    if 0 < coords.x < len(board[0])-1 and 0 < coords.y < len(board)-1:
        # internal point
        return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                               board[coords.y + 1][coords.x],
                                               board[coords.y][coords.x + 1],
                                               board[coords.y][coords.x - 1])
    else:
        left = right = top = bottom = False
        if 0 == coords.x:
            left = True
        elif coords.x == len(board[0]) - 1:
            right = True
        if 0 == coords.y:
            top = True
        elif coords.y == len(board) - 1:
            bottom = True

        if left and top:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x + 1])
        if left and bottom:
            return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                                   board[coords.y][coords.x + 1])
        if right and top:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x - 1])
        if right and bottom:
            return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                                   board[coords.y][coords.x - 1])
        if left:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x + 1],
                                                   board[coords.y - 1][coords.x])
        if right:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x - 1],
                                                   board[coords.y - 1][coords.x])
        if top:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x + 1],
                                                   board[coords.y][coords.x - 1])
        if bottom:
            return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                                   board[coords.y][coords.x + 1],
                                                   board[coords.y][coords.x - 1])
        return RuntimeError(coords, left, right, top, bottom)


def main(input_lines):
    board = [[int(item) for item in line] for line in input_lines]
    print(board)
    minima_counter = 0
    for row_no, row in enumerate(board):
        for col_no, col in enumerate(row):
            coords = Point(col_no, row_no)
            if is_lower_than_neighbours(coords, board):
                minima_counter += board[coords.y][coords.x] + 1
    return minima_counter


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
