import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def main(input_lines):
    depth = 0
    horizontal = 0
    for (direction, distance) in [item.split() for item in input_lines]:
        if direction == 'forward':
            horizontal += int(distance)
        elif direction == 'up':
            depth -= int(distance)
        elif direction == 'down':
            depth += int(distance)

    return depth*horizontal


def functional(input_lines):
    depth = 0
    horizontal = 0
    for (direction, distance) in [item.split() for item in input_lines]:
        if direction == 'forward':
            horizontal += int(distance)
        elif direction == 'up':
            depth -= int(distance)
        elif direction == 'down':
            depth += int(distance)

    return depth*horizontal


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(main(input_lines=input_split_by_lines))
