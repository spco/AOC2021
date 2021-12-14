import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def apply_transformation(fold, dot):
    # Flip dot along fold if necessary, and return dot location
    if fold[0] == 'x':
        if dot[0] > int(fold[1]):
            return (2*int(fold[1]) - dot[0], dot[1])
    else:
        if dot[1] > int(fold[1]):
            return (dot[0], 2*int(fold[1]) - dot[1])
    return dot


def main(input_lines):
    dots = [tuple(int(item) for item in line.split(',')) for line in input_lines
            if ',' in line]

    fold_lines = [line for line in input_lines if 'fold along' in line]
    fold_instructions = [item.lstrip('fold along ').split('=') for item in fold_lines]

    for instruction in fold_instructions:
        dots = [apply_transformation(instruction, dot) for dot in dots]

    for y in range(max(dot[1] for dot in dots)+1):
        for x in range(max(dot[0] for dot in dots)+1):
            if (x, y) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    return


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
