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

    def minx(self):
        return min(self.start.x, self.end.x)

    def maxx(self):
        return max(self.start.x, self.end.x)

    def miny(self):
        return min(self.start.y, self.end.y)

    def maxy(self):
        return max(self.start.y, self.end.y)


def check_vert(line):
    return line.start.x == line.end.x


def check_horiz(line):
    return line.start.y == line.end.y


def val_in_interval(val, start, end):
    return min(start, end) <= val <= max(start, end)


def interval(start1, end1, start2, end2):
    if start2 > end1 or start1 > end2:
        return []
    return [i for i in range(max(start1, start2), min(end1, end2) + 1)]


def intersect_lines(line1, line2):
    """
    Only handles horiz/vert lines
    """
    # Check one is horiz and one vert
    return_vals = []
    if check_vert(line1) and check_horiz(line2):
        print(f'case 1 {line1}, {line2}')
        assert (line1.start.x == line1.end.x)
        assert (line2.start.y == line2.end.y)
        if val_in_interval(line1.start.x, line2.start.x, line2.end.x) and \
                val_in_interval(line2.start.y, line1.start.y, line1.end.y):
            print(f'1 {line1} intersects {line2} ' 
                  f'at {(line1.start.x, line2.start.y)}')
            return_vals.append(Point(line1.start.x, line2.start.y))
        else:
            print(f'1 {line1} DOES NOT intersect {line2}')
    elif check_vert(line2) and check_horiz(line1):
        print(f'case 2 {line1}, {line2}')
        assert (line2.start.x == line2.end.x)
        assert (line1.start.y == line1.end.y)
        if val_in_interval(line2.start.x, line1.start.x, line1.end.x) and \
                val_in_interval(line1.start.y, line2.start.y, line2.end.y):
            print(f'2 {line1} intersects {line2} '
                  f'at {(line2.start.x, line1.start.y)}')
            return_vals.append(Point(line2.start.x, line1.start.y))
        else:
            print(f'2 {line1} DOES NOT intersect {line2}')
    elif check_vert(line1) and check_vert(line2):
        assert (line2.start.x == line2.end.x)
        assert (line1.start.x == line1.end.x)
        print('vert', line1, line2)
        if line1.start.x == line2.start.x:
            ycoords = interval(line1.miny(), line1.maxy(), line2.miny(),
                               line2.maxy())

            # print(ycoords)
            for y in ycoords:
                print(f'3 {line1} intersects {line2} '
                      f'at {(line1.start.x, y)}')
                return_vals.append(Point(line1.start.x, y))
        else:
            print(f'3 {line1} DOES NOT intersect {line2}')
    elif check_horiz(line1) and check_horiz(line2):
        assert (line2.start.y == line2.end.y)
        assert (line1.start.y == line1.end.y)
        print('horiz', line1, line2)
        if line1.start.y == line2.start.y:
            xcoords = interval(line1.minx(), line1.maxx(), line2.minx(),
                               line2.maxx())
            # print(xcoords)
            for x in xcoords:
                print(f'4 {line1} intersects {line2} '
                      f'at {(x, line1.start.y)}')
                return_vals.append(Point(x, line1.start.y))
        else:
            print(f'4 {line1} DOES NOT intersect {line2}')

    # Otherwise check for possibly >1 overlap
    return return_vals


def main(input_lines):
    starts_ends = [line.split(' -> ') for line in input_lines]
    print(starts_ends)
    starts_ends_lists = [[[int(item) for item in x.split(',')], [int(item2) for
                          item2 in y.split(',')]]
                         for [x, y] in starts_ends]
    print(starts_ends_lists)
    starts_ends_points = [[Point(p[0], p[1]) for p in l] for l in starts_ends_lists]
    print(starts_ends_points)
    # exit()
    horiz_vert_lines = [Line(line[0], line[1]) for line in starts_ends_points
                        if line[0].x == line[1].x or line[0].y == line[1].y]

    overlapping_points = []
    # take all pairs of lines
    for (line_no, line) in enumerate(horiz_vert_lines):
        for line2 in horiz_vert_lines[line_no+1:]:
            # print(line, line2)
            intersect_points = intersect_lines(line, line2)
            print(intersect_points)

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
