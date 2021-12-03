"""Day 2 Part 1 and 2 solution."""


INPT = "./input.txt"


def get_puzzle_input(inpt_file=INPT) -> list:
    """Read the input file and returns a list of lines (whitespace striped.)"""

    with open(file=inpt_file, mode="r") as f:
        inpt = []
        for line in f:
            line = line.strip()
            inpt.append(line)
        return inpt


def convert_input_to_tuples(inpt_list:list) -> list:
    """Expects a list of strings with a direction and a number
    separated by a space."""

    tuples = []
    for line in inpt_list:
        line = line.split(" ")
        direction = line[0]
        magnitude = int(line[1])
        tuples.append((direction, magnitude))
    return tuples


def part_01_movement(direction_tuples:list) -> int:
    """Move along the instruction according to part 1 instuctions."""

    horizontal_position = 0
    depth = 0
    for instruction in direction_tuples:
        if instruction[0] == "forward":
            horizontal_position += instruction[1]
        elif instruction[0] == "down":
            depth += instruction[1]
        elif instruction[0] == "up":
            depth -= instruction[1]
            depth = 0 if depth < 0 else depth
    return horizontal_position * depth


def part_02_movement(direction_tuples:list) -> int:
    """Move along the instruction according to part 2 instuctions."""

    horizontal_position = 0
    depth = 0
    aim = 0 
    for instruction in direction_tuples:
        if instruction[0] == "forward":
            horizontal_position += instruction[1]
            depth += (aim * instruction[1])
        elif instruction[0] == "down":
            aim += instruction[1]
        elif instruction[0] == "up":
            aim -= instruction[1]
    return horizontal_position * depth


def main():
    """The main function."""
    puzzle_input = get_puzzle_input()
    direction_tuples = convert_input_to_tuples(inpt_list=puzzle_input)

    part_01_result = part_01_movement(direction_tuples=direction_tuples) 
    print("Part 01:", part_01_result)

    part_02_result = part_02_movement(direction_tuples=direction_tuples)
    print("Part 02:", part_02_result)


if __name__ == "__main__":
    main()

