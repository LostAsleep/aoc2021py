def read_file(fname="./input.txt"):
    """Reads an input file and returns a list of the lines as strings."""
    with open(file=fname) as fhand:
        input_data = [line.strip() for line in fhand.readlines()]
    return input_data
