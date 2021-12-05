"""Day 3 Part 1 solution."""


INPT = "./input.txt"


def get_puzzle_input(inpt_file=INPT) -> list[str]:
    """Read the input file and returns a list of lines (whitespace striped.)"""

    with open(file=inpt_file, mode="r") as f:
        inpt = []
        for line in f:
            line = line.strip()
            inpt.append(line)
        return inpt


def generate_num_lists(inpt_nums_as_str:list[str]):
    """Create integer lists of the string input."""

    conv_inpt = []
    for line in inpt_nums_as_str:
        l_list = [int(x) for x in list(line)]
        conv_inpt.append(l_list)
    return conv_inpt


def count_max_min_binary(list_of_ints:list[int]) -> str:
    """Return the the binary with the most and the least ones an zeros
    according to the problem description of part 1."""

    max_chars = []
    min_chars = []
    for char in range (len(list_of_ints[0])):
        one = 0
        zero = 0
        
        for list in list_of_ints:
            if list[char] == 1:
                one += 1
            elif list[char] == 0:
                zero += 1
        
        if one > zero:
            max_chars.append(1)
            min_chars.append(0)
        elif one < zero:
            max_chars.append(0)
            min_chars.append(1)
    
    max_chars = "".join([str(x) for x in max_chars])
    min_chars = "".join([str(x) for x in min_chars])
    return max_chars, min_chars


def get_positional_lists(list_of_ints:list[int]) -> list[int]:
    result_list = []
    for i in range(len(list_of_ints[0])):
        temp = []
        for int_list in list_of_ints:
            temp.append(int_list[i])
        result_list.append(temp)
    return result_list


def oxy_status(input_list:list):
    pass


def main():
    """The main function."""

    puzzle_input = get_puzzle_input()
    converted_input = generate_num_lists(puzzle_input)
    # print(converted_input)
    maximum, minimum = count_max_min_binary(converted_input)
    product = int(maximum, base=2) * int(minimum, base=2)
    print(product)
    test_postitional_list = get_positional_lists(converted_input)
    print(test_postitional_list)


if __name__ == "__main__":
    main()
