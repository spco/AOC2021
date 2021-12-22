import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


mapping = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def main(input_lines):
    player_position = [int(input_lines[0].split()[-1]), int(input_lines[1].split()[-1])]
    # We want to know: after n 3-rolls, what is the distribution of score-position
    # possibilities for a single player?

    # (score, position): n_possibilities
    # player_1_pos_dist should contain 1 element per set of 3 rolls.
    # Each element should be a dict of {num_universes: player_1_pos}

    player_1_pos_dist = {(0, player_position[0]): 1}
    player_1_dict = {0: player_1_pos_dist}
    max_round = 12
    for i in range(1, max_round):
        next_dict = {}
        for prev_score, prev_pos in player_1_pos_dist.keys():
            if prev_score < 21:
                for m in mapping:
                    # the score to add is the position, which is (previous position + m
                    # -1 ) % 10 + 1
                    new_pos = ((prev_pos + m - 1) % 10) + 1
                    new_score = prev_score + new_pos
                    if (new_score, new_pos) in next_dict:
                        next_dict[(new_score, new_pos)] = \
                            next_dict[(new_score, new_pos)] + \
                            player_1_pos_dist[(prev_score, prev_pos)] * mapping[m]
                    else:
                        next_dict[(new_score, new_pos)] = \
                            player_1_pos_dist[(prev_score, prev_pos)] * mapping[m]
        player_1_pos_dist = next_dict
        player_1_dict[i] = player_1_pos_dist

    player_2_pos_dist = {(0, player_position[1]): 1}
    player_2_dict = {0: player_2_pos_dist}
    for i in range(1, max_round):
        next_dict = {}
        for prev_score, prev_pos in player_2_pos_dist.keys():
            if prev_score < 21:
                for m in mapping:
                    # the score to add is the position, which is (previous position + m
                    # -1 ) % 10 + 1
                    new_pos = ((prev_pos + m - 1) % 10) + 1
                    new_score = prev_score + new_pos
                    if (new_score, new_pos) in next_dict:
                        next_dict[(new_score, new_pos)] = \
                            next_dict[(new_score, new_pos)] + \
                            player_2_pos_dist[(prev_score, prev_pos)] * mapping[m]
                    else:
                        next_dict[(new_score, new_pos)] = \
                            player_2_pos_dist[(prev_score, prev_pos)] * mapping[m]
        player_2_pos_dist = next_dict
        player_2_dict[i] = player_2_pos_dist

    # Now that we have the numbers of possibilities for each player's rolls
    # independently, we now need to play them against each other to see who wins in
    # each case!

    player_1_universes = 0
    player_2_universes = 0
    for round in range(2, len(player_1_dict)):
        # player 1 has go
        print('Player 1', round)
        for play in player_1_dict[round]:
            if play[0] >= 21:
                for play2 in player_2_dict[round-1]:
                    if play2[0] < 21:
                        player_1_universes += player_1_dict[round][play] * \
                                              player_2_dict[round-1][play2]
        print(player_1_universes, player_2_universes)

        # player 2 has go
        print('Player 2', round)
        for play2 in player_2_dict[round]:
            if play2[0] >= 21:
                for play in player_1_dict[round]:
                    if play[0] < 21:
                        player_2_universes += player_2_dict[round][play2] * \
                                              player_1_dict[round][play]
        print(player_1_universes, player_2_universes)
    return max(player_1_universes, player_2_universes)


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
