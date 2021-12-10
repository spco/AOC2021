import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def count(length, lines):
    """
    Returns the number of times words of the given length are found in a list of lines
    """
    word_lengths = len([word for line in lines for word in line if len(word) == length])
    return word_lengths


def main(input_lines):
    input_lines = [item.split('|') for item in input_lines]
    output_lines = [line[1].split() for line in input_lines]
    unique_sizes = {1: 2, 4: 4, 7: 3, 8: 7}
    return sum(count(i, output_lines) for i in unique_sizes.values())


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
