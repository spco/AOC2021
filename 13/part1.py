import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def apply_transformation(fold, dot):
    # Flip dot along fold if necessary, and return dot location
    result = dot
    if fold[0] == 'x':
        if dot[0] > int(fold[1]):
            result = (2*int(fold[1]) - dot[0], dot[1])
    else:
        if dot[1] > int(fold[1]):
            result = (dot[0], 2*int(fold[1]) - dot[1])
    return result


def main(input_lines):
    dot_lines = [tuple(int(item) for item in line.split(',')) for line in input_lines
                 if ',' in line]
    print(dot_lines)
    fold_lines = [line for line in input_lines if 'fold along' in line]
    fold_instructions = [item.lstrip('fold along ').split('=') for item in fold_lines]
    print(fold_instructions)
    print(dot_lines)

    dot_results = [apply_transformation(fold_instructions[0], dot) for dot in dot_lines]

    print(dot_results)

    return len(set(dot_results))


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
