import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def apply_timestep(string, rules):
    output = ''
    for a, b in zip(string[:-1], string[1:]):
        output += a
        if ''.join([a, b]) in rules:
            output += rules[''.join([a, b])]
    output += string[-1]
    return output


def count_chars(string):
    """
    Returns a list of the frequencies of each character in the string
    """
    counts = []
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if string.count(char) > 0:
            counts.append(string.count(char))
    return counts


def main(input_lines):
    # initial string
    string = next(line for line in input_lines if '->' not in line)
    rules_list = [line.split(' -> ') for line in input_lines if '->' in line]
    rules = dict(rules_list)

    for step in range(10):
        #apply the timestep
        string = apply_timestep(string, rules)
        print(step, 'completed', string)

    frequencies = count_chars(string)
    return max(frequencies) - min(frequencies)


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
