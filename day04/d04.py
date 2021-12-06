def get_input(fname="./input.txt") -> list[str]:
    with open(file=fname) as fhand:
        input_data = [line.strip() for line in fhand.readlines()]
    return input_data


class BingoBoard:

    def __init__(self, board_data: list[str]):
        self.board_data = list(board_data)
        self.board = dict()
        print(self.board_data)
        # self.create_board()

    def create_board(self):
        """x = rows, y = columns"""
        self.board = dict()
        print(self.board_data[0])
        board_size = len(self.board_data[0])
        for x in range(board_size):
            for y in range(board_size):
                self.board[(x, y)] = self.board_data[x][y]


def parse_board_input(grid_inpt: list[str]) -> list[str]:

    data_of_boards = []
    temp = []
    for line in grid_inpt:
        line = [x.strip() for x in line.split(" ") if len(x.strip()) > 0] 
        print(line)
        if len(line) == 0:
            data_of_boards.append(temp)
            temp = []
            continue
        temp.append(line)
    data_of_boards.append(temp)
    return data_of_boards


if __name__ == "__main__":
    puzzle_input = get_input()
    drawn_numbers = puzzle_input[0]
    all_boards = parse_board_input(puzzle_input[2:])
    print(all_boards)
