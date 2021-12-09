from utilities import read_file


INPT = "./input_d05.txt"


puzzle_input = read_file(INPT)


def create_line_tuples(input_list):
    result = []
    for line in input_list:
        line = line.split(" -> ")
        pos1 = tuple([int(x) for x in line[0].split(",")])
        pos2 = tuple([int(x) for x in line[1].split(",")])
        line_tuple = (pos1, pos2)
        result.append(line_tuple)
    return list(result)


line_tuples = create_line_tuples(puzzle_input)


def return_points_on_line(line_tuples):
    point_list = []
    for t in line_tuples:
        startx, starty = t[0][0], t[0][1]
        endx, endy = t[1][0], t[1][1]
        # horizontal and vertical condition:
        is_hor_or_vert = startx == endx or starty == endy
        # diagonal condition (diagonal means 45° lines)
        is_diagnonal = abs(startx - endx) == abs(starty - endy)
        xrange = range(startx, endx+1) if startx <= endx else range(endx, startx+1)
        yrange = range(starty, endy+1) if starty <= endy else range(endy, starty+1)
        if is_hor_or_vert:
            line = [(x, y) for x in xrange for y in yrange]
        if is_diagnonal:
            line = []
            x, y = startx, starty
            while True:
                if x == endx and y == endy:
                    break
                if x == startx and y == starty:
                    point = (x, y)
                    line.append(point)
                x = x + 1 if startx < endx else x - 1
                y = y + 1 if starty < endy else y - 1
                point = (x, y)
                line.append(point)
        point_list.append(line)
    return list(point_list)


line_points = return_points_on_line(line_tuples)


def sum_all_line_points(list_of_points):
    grid = dict()
    for line in list_of_points:
        if len(line) == 0:
            continue
        for point in line:
            grid[point] = grid.get(point, 0) + 1
    return dict(grid)


grid_points = sum_all_line_points(line_points)
# print(grid_points)


def print_grid(grid_data):
    points = list(grid_data.keys())
    points = sorted(points)
    result = []
    for c in range(0, 10):
        line_list = []
        for i in range(0, 10):
            if (c, i) in points:
                line_list.append(str(grid_data[(c, i)]))
            else:
                line_list.append(".")
        result.append(line_list)
    return result


# g_points = print_grid(grid_points)
# for line in g_points:
#     print(line)


def count_safe_points(point_dict):
    count = 0
    for value in point_dict.values():
        if value >= 2:
            count += 1
    return count


safe_points = count_safe_points(grid_points)
print("Nr. of safe points:", safe_points)
