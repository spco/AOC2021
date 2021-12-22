import itertools
import os
import datetime


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


def apply_timestep(position, velocity):
    position[0] += velocity[0]
    position[1] += velocity[1]
    velocity[0] = max(velocity[0]-1,0)
    velocity[1] -= 1
    return position, velocity


def main(input_lines):
    print([item.split('..') for item in input_lines[0].split('=')])
    min_x = int([item.split('..') for item in input_lines[0].split('=')][1][0])
    max_x = int([item.split('..') for item in input_lines[0].split('=')][1][1].split(
        ',')[0])
    min_y = int([item.split('..') for item in input_lines[0].split('=')][2][0])
    max_y = int([item.split('..') for item in input_lines[0].split('=')][2][1])

    # maximum_maximum_y = 0
    successful_init_velocities = 0
    for velocity_tuple in itertools.product(range(1, max_x+1), range(min_y, 2000)):
        velocity = [*velocity_tuple]
        if velocity_tuple[1] % 1000 == 0:
            print(datetime.datetime.now(), velocity_tuple)
        # print(velocity)
        position = [0, 0]
        # maximum_y = 0
        # print(position, velocity)
        previous_x = -1
        while position[0] <= max_x and position[1] >= min_y and \
            not (min_x <= position[0] <= max_x and min_y <= position[1] <= max_y)\
                and not (previous_x == position[0] and position[0] < min_x):
            previous_x = position[0]
            position, velocity = apply_timestep(position, velocity)
            # print(position, velocity)
            # print(maximum_y)

        # print(position, velocity, maximum_y, position[0] <= max_x, position[1] >= min_y,
        #       (min_x <= position[0] <= max_x and min_y <= position[1] <= max_y))
        if min_x <= position[0] <= max_x and min_y <= position[1] <= max_y:
            # print(velocity_tuple)
            # print(position, velocity, min_x, max_x, min_y, max_y)
            successful_init_velocities += 1

    return successful_init_velocities


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
