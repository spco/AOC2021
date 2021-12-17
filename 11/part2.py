import os
import numpy as np
import scipy as scipy


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def main(input_lines):
    board = np.array([[int(item) for item in line] for line in input_lines])
    print(board)

    # First test for 10 steps
    total = 0
    for step in range(1,1001):
        # increment energy of all octopi
        board += 1
        print('start step', step)

        flashed = 0*board
        print(board)
        found_9 = True
        while found_9:
            found_9 = False
            with np.nditer(board, flags=['multi_index'], op_flags=['readwrite']) as it:
                for item in it:
                    if item > 9:
                        found_9 = True
                        left = it.multi_index[0] - 1
                        right = it.multi_index[0] + 1
                        up = it.multi_index[1] - 1
                        down = it.multi_index[1] + 1
                        x = it.multi_index[0]
                        y = it.multi_index[1]

                        if left >= 0 and not flashed[left][y]:
                            board[left][y] += 1
                        if left >= 0 and up >= 0 and not flashed[left][up]:
                            board[left][up] += 1
                        if up >= 0 and not flashed[x][up]:
                            board[x][up] += 1
                        if right < board.shape[0] and up >= 0 and not flashed[right][up]:
                            board[right][up] += 1
                        if right < board.shape[0] and not flashed[right][y]:
                            board[right][y] += 1
                        if right < board.shape[0] and down < board.shape[1] and not \
                                flashed[right][down]:
                            board[right][down] += 1
                        if down < board.shape[1] and not flashed[x][down]:
                            board[x][down] += 1
                        if left >= 0 and down < board.shape[1] and not \
                                flashed[left][down]:
                            board[left][down] += 1
                        board[x][y] = 0
                        flashed[x][y] = True
        print('after step', step)
        print(board)
        total += sum(sum(flashed))
        if sum(sum(flashed)) == board.size:
            return step


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
