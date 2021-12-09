import os

unique_sizes = {1: 2, 4: 4, 7: 3, 8: 7}


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def _is(string, value):
    if value in unique_sizes:
        return len(string) == unique_sizes[value]
    else:
        raise RuntimeError(f'Tried to access _is() with value {value}')


def identify_strings(line):
    # top string can be identified by the difference between 7 (3-string) and 1 (
    # 2-string)
    strings = dict()
    strings[8] = 'abcdefg'
    strings[1] = [string for string in line if _is(string, 1)][0]
    strings[7] = [string for string in line if _is(string, 7)][0]
    strings[4] = [string for string in line if _is(string, 4)][0]

    top_segment = set(strings[7]).difference(strings[1]).pop()
    # 9 can be identified as the only 6-string containing all of the characters from 4.
    for word in line:
        if len(word) == 6 and set(strings[4]).issubset(set(word)):
            strings[9] = word

    # Thus bottom-left is the only one not in nine_string
    bottom_left_segment = set(strings[8]).difference(set(strings[9])).pop()

    # 2 is the 5-string containing both top and bottom_left
    for word in line:
        if len(word) == 5 and top_segment in word and bottom_left_segment in word:
            strings[2] = word

    # 0 must be the 6-string that isn't 9 and contains the segments from 1.
    for word in line:
        if len(word) == 6 and set(strings[1]).issubset(word) and set(word) != set(
                strings[9]):
            strings[0] = word

    # 6 must be the 6-string that isn't nine or zero
    for word in line:
        if len(word) == 6 and set(word) != set(strings[9]) and set(word) != set(
                strings[0]):
            strings[6] = word

    # five is the subset of 6 with 5 chars
    for word in line:
        if len(word) == 5 and set(word).issubset(set(strings[6])):
            strings[5] = word

    # three is the remaining 5-string
    for word in line:
        if len(word) == 5 and set(word) != set(strings[5]) and set(word) != set(
                strings[2]) and set(word) != set(strings[5]):
            strings[3] = word

    return strings


def apply_dict(strings_dict, out_line):
    """
    Return an int, which is the 4-digit value made from the individual digits,
    each decoded from the strings_dict
    """
    output = []
    for word in out_line:
        for key, val in strings_dict.items():
            if set(val) == set(word):
                output.append(key)
    return int(''.join([str(i) for i in output]))


def main(input_lines):

    split_lines = [item.split('|') for item in input_lines]
    output_lines = [line[1].split() for line in split_lines]
    input_lines = [line[0].split() for line in split_lines]
    total = sum(apply_dict(identify_strings(in_line), out_line)
                for in_line, out_line in zip(input_lines, output_lines))

    return total


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
