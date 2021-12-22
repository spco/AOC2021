import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def main(input_lines):
    player_position = [int(input_lines[0].split()[-1]), int(input_lines[1].split()[-1])]
    print(player_position)
    player_scores = [0, 0]
    running_total = 0
    i = 0
    for die_rolls in range(1, 10000):
        running_total += die_rolls
        if die_rolls % 3 == 0:
            player_position[i] = (player_position[i] + running_total - 1) % 10 + 1
            # if player_position[i] == 0:
            #     player_scores[i] += 10
            # else:
            player_scores[i] += player_position[i]
            print(die_rolls, player_scores)
            i = (i + 1) % 2
            running_total = 0
            if max(player_scores) >= 1000:
                print(die_rolls, player_scores)
                return die_rolls * min(player_scores)


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
