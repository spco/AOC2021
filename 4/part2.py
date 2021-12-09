import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


class Board:
    def __init__(self, list_of_lists):
        self.board = list_of_lists

    def __repr__(self):
        for row in self.board:
            print(row)
        return ''#str([str(row)+'\n' for row in self.board])

    def completed(self):
        completed = False
        for row in self.board:
            if all(item[1] for item in row):
                completed = True

        for i in range(5):
            if all([self.board[j][i][1] for j in range(5)]):
                completed = True
        return completed

    def unmarked_sum(self):
        total = 0
        for row in self.board:
            for item in row:
                if not item[1]:
                    total += item[0]
        return total


def main(input_lines):
    call_order = [int(item) for item in input_lines[0].split(',')]

    boards = []
    board_counter = 0
    current_board = []
    for counter, line in enumerate(input_lines[2:]):
        print(line, counter, board_counter, boards)
        if counter % 6 == 5:
            board_counter += 1
            boards.append(Board(current_board))
            current_board = []
            print(line, counter, board_counter, current_board, boards)
        else:
            current_board.append([(int(item), False) for item in line.split()])
    boards.append(Board(current_board))
    print(boards)
    # boards is of the form list(Boards)

    def find_in_boards(myboards, char):
        return_values = []
        for board in myboards:
            for sub_list in board.board:
                if (char, False) in sub_list:
                    return_values.append((myboards.index(board),
                                          board.board.index(sub_list),
                                          sub_list.index((char, False))))
                if (char, True) in sub_list:
                    return_values.append((myboards.index(board),
                                          board.board.index(sub_list),
                                          sub_list.index((char, True))))
        return return_values

    def apply_call(boards, call_number):
        coords = find_in_boards(boards, int(call_number))
        for coord in coords:
            this_value = boards[coord[0]].board[coord[1]][coord[2]]
            boards[coord[0]].board[coord[1]][coord[2]] = (this_value[0], True)
        return boards

    def check_board_for_completion(board):
        """
        Board will be a list of lists of tuples
        :param board:
        :return:
        """

    for number in call_order:
        print('\n', int(number), find_in_boards(boards, int(number)))
        boards = apply_call(boards, number)
        boards_to_be_removed = []
        for board_count, board in enumerate(boards):
            if board.completed():
                if len(boards) > 1:
                    boards_to_be_removed.append(board)
                else:
                    print(board_count, board, board.completed())
                    print(number)
                    print(board.unmarked_sum())
                    return number * board.unmarked_sum()

        for board in boards_to_be_removed:
            boards.remove(board)
        print(f'after {number}')
        for board in boards:
            print(board)
            print()
        print()
        print()
    return


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
