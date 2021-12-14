import os
from collections import defaultdict


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def apply_timestep(pairs_dict, rules):
    new_pairs_dict = dict()
    # Grab a pair from the dict
    for pair in pairs_dict.keys():
        # Check whether that pair has a rule, or it should be just treated as is
        if pair in rules:
            # increment the counter for the pair made from the first + output,
            # and output + 2nd.
            for new_key in [pair[0] + rules[pair], rules[pair] + pair[1]]:
                # print('new_key', new_key)
                if new_key in new_pairs_dict:
                    new_pairs_dict[new_key] += pairs_dict[pair]
                else:
                    new_pairs_dict[new_key] = pairs_dict[pair]
        else:
            # Treat as is, increment the counter for this pair
            if pair in new_pairs_dict:
                new_pairs_dict[pair] += pairs_dict[pair]
            else:
                new_pairs_dict[pair] = pairs_dict[pair]

    return new_pairs_dict


def count_chars(pairs_dict):
    """
    Returns a list of the frequencies of each character in the string
    """
    counts = defaultdict(int)

    for key in pairs_dict.keys():
        for pos in key:
            for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if char == pos:
                    counts[char] += pairs_dict[key]

    for key in counts.keys():
        if counts[key] % 2 == 0:
            counts[key] = int(counts[key]/2)
        else:
            counts[key] = int((counts[key]+1) / 2)

    return counts


def main(input_lines):
    # initial string
    string = next(line for line in input_lines if '->' not in line)
    rules_list = [line.split(' -> ') for line in input_lines if '->' in line]
    rules = dict(rules_list)

    pairs_dict = dict()
    for a, b in zip(string[:-1], string[1:]):
        pair = ''.join([a, b])
        if pair in pairs_dict:
            pairs_dict[pair] += 1
        else:
            pairs_dict[pair] = 1

    for step in range(40):
        #apply the timestep
        pairs_dict = apply_timestep(pairs_dict, rules)

    frequencies = count_chars(pairs_dict)


    return max(frequencies.values()) - min(frequencies.values())


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
