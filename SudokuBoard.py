import copy

considered_boards = set()


def to_sudoku_num(char):
    return int(char) if char.isdigit() else 0


def convert_input_row_to_backing_row(row):
    return tuple(map(to_sudoku_num, [char for char in row if char != "."]))


def get_backing_board_from_input_list(input_string_list):
    return tuple(map(convert_input_row_to_backing_row, input_string_list))


def should_be_considered(state):
    return state not in considered_boards


def mark_considered(state):
    considered_boards.add(state)


def has_duplicates(num_list):
    non_zero = [num for num in num_list if num != 0]
    return len(non_zero) != len(set(non_zero))


class SudokuBoard:
    def __init__(self, arg, from_input: False):
        if from_input:
            self.backing_board = get_backing_board_from_input_list(arg)
            self.validate()
        else:
            self.backing_board = arg

    def validate(self):
        for list_ in self.backing_board:
            assert len(list_) == 9
            for num in list_:
                assert num in range(10)

    def get_solutions(self):
        if self.is_full_board():
            print("thinking")
            if self.is_valid_board():
                print("Solution found")
                print(self)
                return {self}
            else:
                return set()
        else:
            solutions = set()
            next_states = self.get_next_possible_states()
            for state in next_states:
                if should_be_considered(state):
                    mark_considered(state)
                    solutions |= state.get_solutions()
            return solutions

    def __str__(self) -> str:
        string = ""
        for row in self.backing_board:
            for i in range(9):
                string += " " if row[i] == 0 else str(row[i])
                if (i + 1) % 3 == 0:
                    string += "|"
            string += "\n"
        return string


    def __eq__(self, o: object) -> bool:
        return isinstance(o, SudokuBoard) and self.backing_board.__eq__(o.backing_board)

    def __hash__(self) -> int:
        return self.backing_board.__hash__()

    def is_full_board(self):
        for list_ in self.backing_board:
            for num in list_:
                if num == 0:
                    return False
        return True

    def is_valid_board(self):
        return not self.has_duplicate_in_rows() and not self.has_duplicate_in_cols() and not self.has_duplicate_in_box()

    def get_next_possible_states(self) -> list:
        forced_next_state = self.get_forced_next_state()
        if forced_next_state is not None:
            return [forced_next_state]
        states = []
        for xy in [(x, y) for x in range(9) for y in range(9)]:
            if self.backing_board[xy[0]][xy[1]] == 0:
                for newVal in range(1, 10):
                    board = copy.deepcopy(self)
                    board.change_value(xy, newVal)
                    if board.is_valid_board():
                        states.append(board)
        return states

    def has_duplicate_in_rows(self):
        return any([has_duplicates(x) for x in self.backing_board])

    def has_duplicate_in_cols(self):
        return any([has_duplicates(map(lambda a: a[i], self.backing_board)) for i in range(9)])

    def has_duplicate_in_box(self):
        return any(has_duplicates(x) for x in self.get_boxes_numbers_lists())

    def get_boxes_numbers_lists(self):
        lists = []
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                new_list = []
                for x in range(2):
                    for y in range(2):
                        new_list.append(self.backing_board[i + x][j + y])
                lists.append(new_list)
        return lists

    def get_forced_next_state(self):
        return None  # TODO check if there's a necessary single next value (like we have 8 in a row/col/box)

    def change_value(self, xy, new_val):
        board_list = [list(l) for l in self.backing_board]
        board_list[xy[0]][xy[1]] = new_val
        self.backing_board = tuple(tuple(i) for i in board_list)
