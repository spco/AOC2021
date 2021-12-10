import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


left_chars = '([{<'
right_chars = ')]}>'
pair_dict = dict(zip(right_chars, left_chars))
reverse_pair_dict = dict(zip(left_chars, right_chars))
char_points = dict(zip(right_chars, [1, 2, 3, 4]))


def main(input_lines):
    board = [[item for item in line] for line in input_lines]
    # Parse all lines - those which reach the end without hitting an illegal
    # character get to have their completion score calculated
    scores = []
    for line in board:
        stack = []
        illegal = False
        for char in line:
            if char in pair_dict.values():
                stack.append(char)
            else:
                if stack[-1] == pair_dict[char]:
                    stack.pop()
                else:
                    illegal = True
                    break
        if not illegal:
            # if you reach here, it's an incomplete line. The pairs of the stack chars
            # (in reverse order) need to be applied to complete the line
            score = 0
            for char in reversed(stack):
                score *= 5
                score += char_points[reverse_pair_dict[char]]

            scores.append(score)

    middle_index = int((len(scores)-1)/2)
    return list(sorted(scores))[middle_index]


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
