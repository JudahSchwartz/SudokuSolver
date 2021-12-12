from SudokuBoard import SudokuBoard

# print("Please enter a sudokuboard to solve. A space can represent an empty box. End each line with a period")
# inputStrings = []
# for x in range(9):
#     inputStrings.append(input())
# board = SudokuBoard(inputStrings, True)

board = SudokuBoard([
        '534678912.',
        '672195348.',
        '1983425 7.',
        '85   1423.',
        '42 853791.',
        '713924 56.',
        '961537284.',
        '28741   5.',
        '34     79.']

        , True)
solutions = board.get_solutions()

print(f"Solved {len(solutions)}")
