"""Day 01 Part 1 and 2."""


INPT = "./input.txt"


def get_puzzle_input() -> list:
    """Read the input file and returns a list of lines (whitespace striped.)"""

    with open(file=INPT, mode="r") as f:
        inpt = []
        for line in f:
            line = line.strip()
            inpt.append(line)
        return inpt


def count_increases(numbers:list) -> int:
    """Count the number of increases while iterating through a list of ints.
    Returns the number of increases."""

    num_inc = 0
    cur_num = None
    for num in numbers:
        if cur_num is None:
            cur_num = num
            continue
        if num > cur_num:
            num_inc += 1
        cur_num = num
    return num_inc


def get_triplet_sums(numbers:list) -> list:
    """Tries to create triplets from a list of ints
    and returns a list of their sums."""

    triples = []
    index = 0
    while True:
        try:
            trip = (numbers[index], numbers[index+1], numbers[index+2])
            trip = sum(trip)
            triples.append(trip)
            index += 1
        except IndexError:
            break
    return triples


def main():
    """The main function."""

    puzzle_input = get_puzzle_input()
    puzzle_input = [int(x) for x in puzzle_input]
    increases = count_increases(puzzle_input)
    print("Part 01 increases:", increases)
    triplet_sums = get_triplet_sums(puzzle_input)
    increases_2 = count_increases(triplet_sums)
    print("Part 02 increases:", increases_2)


if __name__ == "__main__":
    main()
