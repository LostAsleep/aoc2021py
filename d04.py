INPT = "./input_d04.txt"


def get_input(fname=INPT):
    with open(file=fname) as fhand:
        input_data = [line.strip() for line in fhand.readlines()]
    return input_data


class BingoBoard:

    def __init__(self, board_data):
        self.board_data = list(board_data)
        self.board = dict()
        self.create_board()
        self.last_num = None
        self.win = False

    def create_board(self):
        """x = rows, y = columns"""
        board_size = len(self.board_data[0])
        for x in range(board_size):
            for y in range(board_size):
                self.board[(x, y)] = (self.board_data[x][y], False)

    def update_drawn_number(self, num):
        if self.win is False:
            self.last_num = int(num)
            for pos in self.board.keys():
                if self.win is True:
                    break
                if num == self.board[pos][0]:
                    self.board[pos] = (self.board[pos][0], True)
                    self.check_for_win()

    def check_for_win(self):
        if self.win is False:
            for row in range(0, 5):
                if self.win is True:
                    break
                num_row_true = 0
                for col in range(0, 5):
                    if self.win is True:
                        break
                    if self.board[(row, col)][1] is True:
                        num_row_true += 1
                        if num_row_true == 5:
                            self.win = True

            for col in range(0, 5):
                if self.win is True:
                    break
                num_col_true = 0
                for row in range(0, 5):
                    if self.win is True:
                        break
                    if self.board[(row, col)][1] is True:
                        num_col_true += 1
                        if num_col_true == 5:
                            self.win = True
        if self.win is True:
            print("WIN")
            unmarked_nums = [int(val[0]) for val in self.board.values() if val[1] is False]
            print("Sum of unmarked numbers x last num:", sum(unmarked_nums) * self.last_num)


def parse_board_input(grid_inpt):
    """Get rid of empty lines/lists and return a list containing
    the lists of the board rows."""
    data_of_boards = []
    temp = []
    for line in grid_inpt:
        line = [x.strip() for x in line.split(" ") if len(x.strip()) > 0] 
        if len(line) == 0:
            data_of_boards.append(temp)
            temp = []
            continue
        temp.append(line)
    data_of_boards.append(temp)
    return data_of_boards


def create_bingo_boards(board_lists):
    """Loop through parsed bing board data and create bingo board objects."""
    all_bingo_boards = []
    for board_data in board_lists:
        all_bingo_boards.append(BingoBoard(board_data))
    return all_bingo_boards


def part_1_solution(parsed_board_data, numbers):
    """Get first winning bingo board."""
    all_boards = create_bingo_boards(parsed_board_data)
    winner = False
    for number in numbers:
        if winner is True:
            break
        print(number)
        for board in all_boards:
            if winner is True:
                break
            board.update_drawn_number(number)
            if board.win is True:
                winner = True


def part_2_solution(parsed_board_data, numbers):
    """Get last winning bingo board."""
    all_boards = create_bingo_boards(parsed_board_data)
    winning_boards = []
    for number in numbers:
        print(number)
        for board in all_boards:
            if board.win is True:
                continue
            board.update_drawn_number(number)
            if board.win is True:
                winning_boards.append(board)
    winning_boards[-1].check_for_win()


if __name__ == "__main__":
    puzzle_input = get_input()
    drawn_numbers = puzzle_input[0].strip().split(",")
    all_board_data = parse_board_input(puzzle_input[2:])

    part_1_solution(all_board_data, drawn_numbers)
    part_2_solution(all_board_data, drawn_numbers)