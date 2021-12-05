import copy

considered_boards = set()


def to_sudoku_num(char):
    return int(char) if char.isdigit() else 0


def convert_input_row_to_backing_row(row):
    return list(map(to_sudoku_num, [char for char in row if char != "."]))


def get_backing_board_from_input_list(input_string_list):
    return list(map(convert_input_row_to_backing_row, input_string_list))


def should_be_considered(state):
    return not considered_boards.__contains__(state)


def mark_considered(state):
    considered_boards.add(state)


def has_duplicates(num_list):
    non_zero = [num for num in num_list if num != 0]
    return len(non_zero) != len(set(non_zero))


class SudokuBoard:
    def __init__(self, arg, from_input: False):
        if from_input:
            self.backingBoard = get_backing_board_from_input_list(arg)
            self.validate()
        else:
            self.backingBoard = arg

    def validate(self):
        for list_ in self.backingBoard:
            assert len(list_) == 9
            for num in list_:
                assert num in range(10)

    def get_solutions(self):
        if self.is_full_board():
            if self.is_valid_board():
                return [self]
            else:
                return []
        else:
            solutions = []
            next_states = self.get_next_possible_states()
            for state in next_states:
                if should_be_considered(state):
                    mark_considered(state)
                    solutions.extend(state.get_solutions())
            return solutions

    def is_full_board(self):
        for list_ in self.backingBoard:
            for num in list_:
                if num == 0:
                    return False
        return True

    def is_valid_board(self):
        return not self.has_duplicate_in_rows() and not self.has_duplicate_in_cols() and not self.has_duplicate_in_box()

    def get_next_possible_states(self) -> list:
        states = []
        for xy in [(x, y) for x in range(9) for y in range(9)]:
            if self.backingBoard[xy[0]][xy[1]] == 0:
                for newVal in range(1, 10):
                    board = copy.deepcopy(self)
                    board.backingBoard[xy[0]][xy[1]] = newVal
                    if board.is_valid_board():
                        states.append(board)
        return states

    def has_duplicate_in_rows(self):
        return any([has_duplicates(x) for x in self.backingBoard])

    def has_duplicate_in_cols(self):
        any([has_duplicates(map(lambda a: a[i], self.backingBoard)) for i in range(9)])

    def has_duplicate_in_box(self):
        return any(has_duplicates(x) for x in self.get_boxes_numbers_lists())

    def get_boxes_numbers_lists(self):
        lists = []
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                new_list = []
                for x in range(2):
                    for y in range(2):
                        new_list.append(self.backingBoard[i + x][j + y])
                lists.append(new_list)
        return lists
