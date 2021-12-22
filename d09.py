"""Advent of code 2021 - Day 09"""

from utilities import read_file


INPT = "./input_d09.txt"
inpt = read_file(INPT)
# print(inpt)


def generate_map(list_of_str):
    """Generate a dict heightmap.
    Returns the map, and max row and col values."""

    heightmap = dict()
    max_row_len = len(list_of_str)
    max_col_len = len(list_of_str[0])
    for x in range(max_row_len):
        for y in range(max_col_len):
            heightmap[(x, y)] = int(list_of_str[x][y])
    return dict(heightmap), max_row_len-1, max_col_len-1


def get_neighbors(int_tuple, max_x, max_y):
    """Returns the direct adjacent neigbour coordinates on a grid."""
    neighbors = []
    x, y = int_tuple[0], int_tuple[1]
    all_neighbors = [
        (x-1, y),
        (x+1, y),
        (x, y-1),
        (x, y+1),
        ]
    for t in all_neighbors:
        if t[0] < 0 or t[0] > max_x or t[1] < 0 or t[1] > max_y:
            continue
        neighbors.append(t)
    return neighbors


def get_low_points(h_map, max_x, max_y):
    """Checks all points in heat map against their neighbors.

    Returns a list with the low point height values as int."""
    low_points = []
    for k, v in h_map.items():
        is_low = True
        neighbors = get_neighbors(k, max_x, max_y)
        for n in neighbors:
            if h_map[n] <= v:
                is_low = False
                break
        if is_low:
            low_points.append(v)
    return list(low_points)


def calculate_risk_level(list_of_ints):
    """Returns the sum all list items + 1."""
    return sum([x + 1 for x in list_of_ints])


heightmap, max_x, max_y = generate_map(inpt)
# print(heightmap)

# n = get_neighbors((4, 9), max_x, max_y)
# print(n)

lows = get_low_points(heightmap, max_x, max_y)
print(lows)

risk_level = calculate_risk_level(lows)
print(f"Risk Level: {risk_level}")
