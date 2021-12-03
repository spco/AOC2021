import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def criteria(list_of_strings, position, mode):
    """Given a list of strings and a position, return only the values with the most 
    common/uncommon value in that position, depending on the mode selected"""
    zero_strings = []
    one_strings = []
    for string in list_of_strings:
        if string[position] == '0':
            zero_strings.append(string)
        else:
            one_strings.append(string)
    if mode == 'common':
        if len(zero_strings) > len(one_strings):
            return zero_strings
        else:
            return one_strings
    else:
        if len(zero_strings) <= len(one_strings):
            return zero_strings
        else:
            return one_strings


def functional_criteria(list_of_strings, position, return_common):
    """Given a list of strings and a position, return only the values with the most
    common/uncommon value in that position, depending on the mode selected"""
    zero_strings = list(filter(lambda x: x[position] == '0',
                               list_of_strings
                               ))
    one_strings = list(filter(lambda x: x[position] == '1',
                              list_of_strings
                              ))

    # Exclusive or is used to ensure exactly one of the conditions is true,
    # and direct it accordingly. We want 'common' mode to return zero strings if the
    # lengths condition is false, and 'uncommon' to return zero if it's true.
    return one_strings if return_common ^ (len(zero_strings) <= len(one_strings)) \
        else zero_strings


def main(input_lines):
    # Calculate oxy by iteratively sub-setting the lines until only one remains
    lines = input_lines
    position = 0
    while len(lines) > 1:
        lines = criteria(lines, position, 'common')
        position += 1
    oxy = lines[0]

    # Calculate co2 by iteratively sub-setting the lines until only one remains
    lines = input_lines
    position = 0
    while len(lines) > 1:
        lines = criteria(lines, position, 'uncommon')
        position += 1
    co2 = lines[0]

    # Convert strings to bytearrays, then convert those from base 2 to base 10 ints
    return int(bytearray(oxy, 'utf-8'), 2)*int(bytearray(co2, 'utf-8'), 2)


def functional(input_lines):
    # Calculate oxy by iteratively sub-setting the lines until only one remains
    lines = input_lines
    position = 0
    while len(lines) > 1:
        lines = functional_criteria(lines, position, True)
        position += 1
    oxy = lines[0]

    # Calculate co2 by iteratively sub-setting the lines until only one remains
    lines = input_lines
    position = 0
    while len(lines) > 1:
        lines = functional_criteria(lines, position, False)
        position += 1
    co2 = lines[0]

    # Convert strings to bytearrays, then convert those from base 2 to base 10 ints
    return int(bytearray(oxy, 'utf-8'), 2)*int(bytearray(co2, 'utf-8'), 2)


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
