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
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash(repr(self))


def unique(list_of_points):
    return_list = []
    for point in list_of_points:
        if point not in return_list:
            return_list.append(point)
    return return_list


def is_lower_than_neighbours(coords, board):
    if 0 < coords.x < len(board[0])-1 and 0 < coords.y < len(board)-1:
        # internal point
        return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                               board[coords.y + 1][coords.x],
                                               board[coords.y][coords.x + 1],
                                               board[coords.y][coords.x - 1])
    else:
        left = right = top = bottom = False
        if 0 == coords.x:
            left = True
        elif coords.x == len(board[0]) - 1:
            right = True
        if 0 == coords.y:
            top = True
        elif coords.y == len(board) - 1:
            bottom = True

        if left and top:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x + 1])
        if left and bottom:
            return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                                   board[coords.y][coords.x + 1])
        if right and top:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x - 1])
        if right and bottom:
            return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                                   board[coords.y][coords.x - 1])
        if left:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x + 1],
                                                   board[coords.y - 1][coords.x])
        if right:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x - 1],
                                                   board[coords.y - 1][coords.x])
        if top:
            return board[coords.y][coords.x] < min(board[coords.y + 1][coords.x],
                                                   board[coords.y][coords.x + 1],
                                                   board[coords.y][coords.x - 1])
        if bottom:
            return board[coords.y][coords.x] < min(board[coords.y - 1][coords.x],
                                                   board[coords.y][coords.x + 1],
                                                   board[coords.y][coords.x - 1])
        return RuntimeError(coords, left, right, top, bottom)


def find_lower_point(centre_point, points, board):
    for point in points:
        if board[point.y][point.x] < board[centre_point.y][centre_point.x]:
            return find_local_minima(point, board)

    return centre_point


def find_local_minima(coords, board):
    if 0 < coords.x < len(board[0])-1 and 0 < coords.y < len(board)-1:
        # internal point
        return find_lower_point(coords,
                                [Point(coords.x, coords.y - 1),
                                 Point(coords.x, coords.y + 1),
                                 Point(coords.x - 1, coords.y),
                                 Point(coords.x + 1, coords.y)],
                                board)
    else:
        left = right = top = bottom = False
        if 0 == coords.x:
            left = True
        elif coords.x == len(board[0]) - 1:
            right = True
        if 0 == coords.y:
            top = True
        elif coords.y == len(board) - 1:
            bottom = True

        if left and top:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y + 1),
                                     Point(coords.x + 1, coords.y)],
                                    board)
        if left and bottom:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y - 1),
                                     Point(coords.x + 1, coords.y)],
                                    board)
        if right and top:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y + 1),
                                     Point(coords.x - 1, coords.y)],
                                    board)
        if right and bottom:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y - 1),
                                     Point(coords.x - 1, coords.y)],
                                    board)
        if left:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y - 1),
                                     Point(coords.x, coords.y + 1),
                                     Point(coords.x + 1, coords.y)],
                                    board)
        if right:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y - 1),
                                     Point(coords.x, coords.y + 1),
                                     Point(coords.x - 1, coords.y)],
                                    board)
        if top:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y + 1),
                                     Point(coords.x - 1, coords.y),
                                     Point(coords.x + 1, coords.y)],
                                    board)
        if bottom:
            return find_lower_point(coords,
                                    [Point(coords.x, coords.y - 1),
                                     Point(coords.x - 1, coords.y),
                                     Point(coords.x + 1, coords.y)],
                                    board)
        return RuntimeError(coords, left, right, top, bottom)


def main(input_lines):
    board = [[int(item) for item in line] for line in input_lines]

    minima_list = []
    for row_no, row in enumerate(board):
        for col_no, col in enumerate(row):
            coords = Point(col_no, row_no)
            if is_lower_than_neighbours(coords, board):
                minima_list.append(Point(coords.x, coords.y))

    # Iterate over all points in the board. If they're not a 9, then trace them
    # downhill to a minima (for speed, we could even check against all previously
    # tackled points). Then append them to the list of points in the associated basin.
    #
    # basins is a dict with keys being minima and vals being all points in that
    # minima's basin
    basins = dict()
    for item in minima_list:
        basins[item] = []
    for row_no, row in enumerate(board):
        for col_no, col in enumerate(row):
            print(row_no, col_no, board[row_no][col_no])
            if col != 9:
                # identify local minima of point
                p = Point(col_no, row_no)
                minima = find_local_minima(p, board)
                # add this point to the list against that point
                basins[minima].append(Point(p.x, p.y))

    # for each minima in the dict, calculate its basin size by removing duplicates,
    # and counting the points
    basin_sizes = dict()
    for minima in minima_list:
        basins[minima] = unique(basins[minima])
        basin_sizes[minima] = len(basins[minima])

    # get largest 3 basins
    largest_basins = sorted(basin_sizes.values())[-3:]
    # multiply together
    return largest_basins[0] * largest_basins[1] * largest_basins[2]


def functional(input_lines):
    pass


if __name__ == "__main__":
    input_split_by_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'input.txt'))
    print(main(input_lines=input_split_by_lines))
    print(functional(input_lines=input_split_by_lines))
