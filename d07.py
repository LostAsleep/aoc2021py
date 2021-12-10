from utilities import read_file


INPT = "input_d07.txt"

inpt = [int(x) for x in read_file(INPT)[0].split(",")]
print(inpt)

def align_crabs(p_inpt):
    min_pos = min(p_inpt)
    max_pos = max(p_inpt)
    possible_positions = list(range(min_pos, max_pos))

    # Part 1
    distances = dict()
    for i in possible_positions:
        distance_diffs = [abs(i - x) for x in p_inpt]
        distances[i] = sum(distance_diffs)
    best_pos = None
    for k, v in distances.items():
        if best_pos is None:
            best_pos = k
        if v < distances[best_pos]:
            best_pos = k
    print("Part 1:")
    print(f"Best postion is {best_pos} with {distances[best_pos]} fuel consumption.\n")

    # Part 2
    def calc_fuel(num):
        fuel = 0
        for i in range (1, num+1):
            fuel += i
        return fuel


    dist_2 = dict()
    for i in possible_positions:
        test = [sum(list(range(1, abs(i - x) + 1))) for x in p_inpt]
        dist_2[i] = sum(test)

    best = None
    for k, v in dist_2.items():
        if best is None:
            best = k
        if v < dist_2[best]:
            best = k
    print("Part 2:")
    print(f"Best postion is {best} with {dist_2[best]} fuel consumption.\n")

align_crabs(inpt)
