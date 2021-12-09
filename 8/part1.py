import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def count(value, lines):
    word_lengths = [len(word) for line in lines for word in line]
    counter = 0
    for word in word_lengths:
        if word == value:
            counter += 1
    return counter


def main(input_lines):
    input_lines = [item.split('|') for item in input_lines]
    output_lines = [line[1].split() for line in input_lines]
    unique_sizes = {1: 2, 4: 4, 7: 3, 8: 7}
    ones = count(unique_sizes[1], output_lines)
    fours = count(unique_sizes[4], output_lines)
    sevens = count(unique_sizes[7], output_lines)
    eights = count(unique_sizes[8], output_lines)
    return ones + fours + sevens + eights


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
