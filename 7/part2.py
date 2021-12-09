import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def triangular_number(number):
    return int(number*(number+1)/2)


def main(input_lines):
    crab_positions = [int(item) for item in input_lines[0].split(',')]
    print(crab_positions)
    max_pos = max(crab_positions)
    min_pos = min(crab_positions)
    fuel_costs = []
    for position in range(min_pos, max_pos+1):
        fuel_costs.append(sum(triangular_number(abs(position - crab_pos)) for
                              crab_pos in crab_positions))

    print(fuel_costs)
    return min(fuel_costs)


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
