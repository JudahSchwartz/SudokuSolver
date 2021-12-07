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
    assert False


def test_has_duplicate_in_cols():
    assert False


def test_has_duplicate_in_box():
    assert False


def test_get_boxes_numbers_lists():
    assert False
