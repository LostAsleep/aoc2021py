def get_input(fname="./input.txt") -> list[str]:
    with open(file=fname) as fhand:
        input_data = [line.strip() for line in fhand.readlines()]
    return input_data


def get_pos_list(data:list[str]) -> list[str]:
    positional_list = []
    for i in range(len(input_data[0])):
        temp = [d[i] for d in input_data]
        positional_list.append(temp)
    return positional_list


def get_most_least_equal(some_list):
    zeros = some_list.count("0")
    ones = some_list.count("1")
    if zeros > ones:
        return "0", "1", False
    elif ones > zeros:
        return "1", "0", False
    elif zeros == ones:
        return "0", "1", True


def part_01_solution(pos_list):
    max_string = ""
    min_string = ""
    for chars in positional_list:
        most, least, equal = get_most_least_equal(chars)
        if not equal:
            max_string += most
            min_string += least
        else:
            continue
    print(f"Max: {max_string} = {int(max_string, base=2)}")
    print(f"Min: {min_string} = {int(min_string, base=2)}")
    print(f"Product: {int(max_string, base=2) * int(min_string, base=2)}")


def part_02_solution(list_input):
    possible_oxy = list(list_input)
    possible_co2 = list(list_input)

    while len(possible_oxy) > 1:
        print(possible_oxy)
        for i in range(len(possible_oxy[0])):
            print(len(possible_oxy[0]))
            pos_list = get_pos_list(possible_oxy)
            most, least, equal = get_most_least_equal(pos_list)
            temp_list = []
            print(most, least, equal)
            if not equal:
                for bits in possible_oxy:
                    if bits[i] == most:
                        temp_list.append(bits)
            if equal:
                for bits in possible_oxy:
                    if bits[i] == "1":
                        temp_list.append(bits)
            possible_oxy = list(temp_list)

    while len(possible_co2) > 1:
        for i in range(len(possible_co2[0])):
            pos_list = get_pos_list(possible_co2)
            most, least, equal = get_most_least_equal(pos_list)
            temp_list = []
            if not equal:
                for bits in possible_co2:
                    if bits[i] == least:
                        temp_list.append(bits)
            if equal:
                for bits in possible_co2:
                    if bits[i] == "0":
                        temp_list.append(bits)
            possible_co2 = list(temp_list)

    print(possible_oxy)
    print(possible_co2)


if __name__ == "__main__":
    input_data = get_input()
    positional_list = get_pos_list(data=input_data)
    part_01_solution(pos_list=positional_list)
    part_02_solution(input_data)

