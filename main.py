from SudokuBoard import SudokuBoard

print("Please enter a sudokuboard to solve. A space can represent an empty box. End each line with a period")
inputStrings = []
for x in range(9):
    inputStrings.append(input())
board = SudokuBoard(inputStrings, True)
solutions = board.get_solutions()

print(f"Solved {len(solutions)}")
