import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [int(item.rstrip()) for item in input_file.readlines()]
    return input_split_lines


def main(input_lines):
    counter = 0
    for item, next_item in zip(input_lines[:-1], input_lines[1:]):
        if item < next_item:
            counter += 1

    counter = 0
    prev_value = input_lines[0]
    for item in input_lines[1:]:
        if item > prev_value:
            counter += 1
        prev_value = item

    return counter


def functional(input_lines):
    counter = sum([item for item in map(lambda x, y: x < y,
                                        input_lines[:-1],
                                        input_lines[1:])])
    return counter


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
