import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [int(item.rstrip()) for item in input_file.readlines()]
    return input_split_lines


def main(input_lines):
    counter = 0
    prev_sum = sum(input_lines[0:3]) + 1
    for item1, item2, item3 in zip(input_lines[:-2],
                                   input_lines[1:-1],
                                   input_lines[2:]):
        if sum([item1, item2, item3]) > prev_sum:
            counter += 1
        prev_sum = sum([item1, item2, item3])

    return counter


def functional(input_lines):
    counter = sum([item for item in map(lambda x, y: x < y,
                                        input_lines[:-3],
                                        input_lines[3:])])
    return counter


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
