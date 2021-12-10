import os


def read_input(input_filename):
    with open(input_filename) as input_file:
        input_split_lines = [item.rstrip() for item in input_file.readlines()]
    return input_split_lines


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(repr(self))


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return str(f'{self.start} -> {self.end}')

    def points(self):
        x_diff = self.end.x - self.start.x
        if x_diff != 0:
            x_step = int(x_diff/abs(x_diff))
        else:
            x_step = 0
        y_diff = self.end.y - self.start.y
        if y_diff != 0:
            y_step = int(y_diff/abs(y_diff))
        else:
            y_step = 0
        length = max(abs(x_diff), abs(y_diff)) + 1

        points_list = [Point(int(self.start.x + i * x_step),
                             int(self.start.y + i * y_step)) for i in range(length)]
        return points_list


def intersect_lines(line1, line2):
    return set(line1.points()).intersection(line2.points())


def main(input_lines):
    starts_ends = [line.split(' -> ') for line in input_lines]
    starts_ends_lists = [[[int(item) for item in x.split(',')], [int(item2) for
                          item2 in y.split(',')]]
                         for [x, y] in starts_ends]
    starts_ends_points = [[Point(p[0], p[1]) for p in l] for l in starts_ends_lists]
    lines = [Line(line[0], line[1]) for line in starts_ends_points]

    overlapping_points = []
    # take all pairs of lines
    for (line_no, line) in enumerate(lines):
        print(f'{line_no}')
        for line2 in lines[line_no+1:]:
            intersect_points = intersect_lines(line, line2)
            for point in intersect_points:
                overlapping_points.append(point)

    return len(set(overlapping_points))


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
