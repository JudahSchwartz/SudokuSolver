from SudokuBoard import SudokuBoard


# '''534678912.
#     672195348.
#     198342567.
#     859761423.
#     426853791.
#     712924856.
#     961537284.
#     287419635.
#     345286179.
#     '''

def test_validate_pass():
    board = SudokuBoard([
        '534678912.',
        '672195348.',
        '1983425 7.',
        '859761423.',
        '42 853791.',
        '713924 56.',
        '961537284.',
        '287419635.',
        '345286179.']

        , True)
    board.validate()


def test_get_solutions_1solved_solved():
    board = SudokuBoard([
        '534678912.',
        '672195348.',
        '1983425 7.',
        '859761423.',
        '42 853791.',
        '713924 56.',
        '961537284.',
        '287419635.',
        '345286179.']

        , True)
    solutions = board.get_solutions()
    assert len(solutions) == 1
    assert solutions.pop().backing_board[2][7] == 6


def test_has_duplicate_in_rows():
    pass


def test_has_duplicate_in_cols():
    assert SudokuBoard([
        '534678912.',
        '672195348.',
        '198342567.',
        '859761423.',
        '426853791.',
        '713924 86.',
        '961537284.',
        '287419635.',
        '345286179.'], True).has_duplicate_in_cols()


def test_has_duplicate_in_box():
    assert False


def test_get_boxes_numbers_lists():
    assert False


def test_sudoku_board_str():
    assert '''534|678|912|
672|195|348|
198|342|5 7|
859|761|423|
42 |853|791|
713|924| 56|
961|537|284|
287|419|635|
345|286|179|
''' == SudokuBoard([
        '534678912.',
        '672195348.',
        '1983425 7.',
        '859761423.',
        '42 853791.',
        '713924 56.',
        '961537284.',
        '287419635.',
        '345286179.']

        , True).__str__()
