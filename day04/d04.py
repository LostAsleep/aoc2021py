def get_input(fname="./input.txt") -> list[str]:
    with open(file=fname) as fhand:
        input_data = [line.strip() for line in fhand.readlines()]
    return input_data


class BingoBoard():

    def __init__(self, list_of_rows):
        self.list_of_rows = list(list_of_rows)
        self.board = dict()
        print(self.list_of_rows)
        # self.create_board()

    def convert_input_to_lists(self):
        self.input_lists = []
        for row in self.list_of_rows:
            row = [num.strip() for num in row]
            self.input_lists.append(row)
        
    def create_board(self):
        """x = rows, y = columns"""
        self.board = dict()
        list_input = self.convert_input_to_lists()
        print(list_input[0])
        board_size = len(list_input[0])
        for x in range(board_size):
            for y in range(board_size):
                self.board[(x, y)] = list_input[x][y]


def generate_boards(grid_inpt):
    data_of_boards = []
    temp = []
    count = 0
    for line in grid_inpt:
        if len(line) == 0:
            data_of_boards.append(temp)
            count = 0
            temp = []
            continue
        count += 1
        temp.append(line)
        print("Nr of boards:", len(data_of_boards))
    return [BingoBoard(data) for data in data_of_boards]   


if __name__ == "__main__":
    puzzle_input = get_input()
    drawn_numbers = puzzle_input[0]
    print(puzzle_input)
    all_boards = generate_boards(puzzle_input[2:])
    for board in all_boards:
        print(len(all_boards))
        print(board.board)
    
