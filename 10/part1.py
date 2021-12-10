import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


left_chars = '([{<'
right_chars = ')]}>'
pair_dict = dict(zip(right_chars, left_chars))
print(pair_dict)
char_points = dict(zip(right_chars, [3, 57, 1197, 25137]))


def main(input_lines):
    board = [[item for item in line] for line in input_lines]
    print(board)
    total_points = 0
    for line in board:
        stack = []
        for char in line:
            if char in pair_dict.values():
                stack.append(char)
            else:
                if stack[-1] == pair_dict[char]:
                    stack.pop()
                else:
                    print(line)
                    print(stack)
                    print(char)
                    total_points += char_points[char]
                    break
    return total_points


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
