import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def main(input_lines):
    fish = [int(item) for item in input_lines[0].split(',')]
    fish_count = dict.fromkeys(range(9), 0)
    for f in fish:
        fish_count[f] += 1
    for time in range(256):
        new_fish_count = dict.fromkeys(range(9), 0)
        for f, f_val in fish_count.items():
            if f == 0:
                new_fish_count[8] = f_val
                new_fish_count[6] += f_val
            else:
                new_fish_count[f - 1] += f_val
        fish_count = new_fish_count

    return sum(num for num in fish_count.values())


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
