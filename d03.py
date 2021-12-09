from collections import Counter


INPT = "./input_d03.txt"


def get_input(fname=INPT):
    with open(file=fname) as fhand:
        input_data = [line.strip() for line in fhand.readlines()]
    return input_data


def get_pos_list(data):
    positional_list = []
    for i in range(len(input_data[0])):
        temp = [d[i] for d in input_data]
        positional_list.append(temp)
    return list(positional_list)


def part_01_solution(list_input):
    pos_list = get_pos_list(list_input)
    max_string = ""
    min_string = ""
    for chars in pos_list:
        most_com = Counter(chars).most_common(2)
        most = most_com[0][0]
        least = most_com[1][0]
        if most_com[0][1] != most_com[1][1]:
            max_string += most
            min_string += least
    
    print(f"Gamma Rate (Max): {max_string} = {int(max_string, base=2)}")
    print(f"Epsilon Rate (Min): {min_string} = {int(min_string, base=2)}")
    print(f"Power Consumption: {int(max_string, base=2) * int(min_string, base=2)}\n")


def part_02_solution(list_input):
    possible_oxy = list(list_input)
    possible_co2 = list(list_input)

    for i in range(len(possible_oxy[0])):  # To get length of bit sequence
        if len (possible_oxy) == 1:
            break
        pos_list = [b[i] for b in possible_oxy]
        count = Counter(pos_list)
        temp_list = []
        zeros, ones = count["0"], count["1"]
        for bits in possible_oxy:
            if zeros > ones and bits[i] == "0":
                temp_list.append(bits)
            elif ones > zeros and bits[i] == "1":
                temp_list.append(bits)
            elif ones == zeros and bits[i] == "1":
                temp_list.append(bits)
        possible_oxy = list(temp_list)

    for i in range(len(possible_co2[0])):  # To get length of bit sequence
        if len(possible_co2) == 1:
            break
        pos_list = [b[i] for b in possible_co2]
        count = Counter(pos_list)
        temp_list = []
        zeros, ones = count["0"], count["1"]
        for bits in possible_co2:
            if zeros < ones and bits[i] == "0":
                temp_list.append(bits)
            elif ones < zeros and bits[i] == "1":
                temp_list.append(bits)
            elif ones == zeros and bits[i] == "0":
                temp_list.append(bits)
        possible_co2 = list(temp_list)

    print(f"Oxygen Generator: {possible_oxy[0]} = {int(possible_oxy[0], base=2)}")
    print(f"CO2 Scrubber: {possible_co2[0]} = {int(possible_co2[0], base=2)}")
    print(f"Life Support rating: {int(possible_oxy[0], base=2) * int(possible_co2[0], base=2)}\n")


if __name__ == "__main__":
    input_data = get_input()
    part_01_solution(input_data)
    part_02_solution(input_data)
