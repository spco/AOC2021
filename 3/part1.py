import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def main(input_lines):

    counters = [0]*len(input_lines[0])
    total_lines = len(input_lines)
    # count the 1s in each position. We know the number of zeros
    # will be (total_lines - counters[i])
    for item in input_lines:
        for char_pos, char in enumerate(item):
            if char == '1':
                counters[char_pos] += 1

    # Build strings from '0' and '1' chars depending on the values in counters
    gamma_str = ''
    epsilon_str = ''
    for count in counters:
        if count > total_lines/2:
            # 1 is more frequent, so set 1 in gamma, 0 in epsilon
            gamma_str += '1'
            epsilon_str += '0'
        else:
            gamma_str += '0'
            epsilon_str += '1'

    # Convert strings to bytearrays, then convert those from base 2 to base 10 ints
    return int(bytearray(gamma_str, 'utf-8'), 2) * \
        int(bytearray(epsilon_str, 'utf-8'), 2)


def functional(input_lines):

    counters = [0]*len(input_lines[0])
    total_lines = len(input_lines)
    # count the 1s in each position. We know the number of zeros
    # will be (total_lines - counters[i])
    for item in input_lines:
        for char_pos, char in enumerate(item):
            if char == '1':
                counters[char_pos] += 1

    # return True if 1s more frequent than 0s, else False
    one_more_freq = list(map(lambda count: count > total_lines/2, counters))

    gamma_str = ''.join(map(lambda x: '1' if x else '0', one_more_freq))
    epsilon_str = ''.join(map(lambda x: '0' if x else '1', one_more_freq))

    # Convert strings to bytearrays, then convert those from base 2 to base 10 ints
    return int(bytearray(gamma_str, 'utf-8'), 2) * \
        int(bytearray(epsilon_str, 'utf-8'), 2)


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
