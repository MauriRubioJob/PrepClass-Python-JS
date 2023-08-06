import sudoku


def check_position(puzzle, row, col, n):
    # check the row
    for i in range(len(puzzle[row])):
        number = puzzle[row][i]
        if n == number:
            return False

    # check the column
    for i in range(len(puzzle[col])):
        number = puzzle[i][col]
        if n == number:
            return False

    # check the section
    section_row = row // 3 * 3
    section_col = col // 3 * 3
    for i in range(section_row, section_row + 3):
        for j in range(section_col, section_col + 3):
            number = puzzle[i][j]
            if n == number:
                return False

    return True
#  hueristic, backtracking, brute-force, algorithm


def solve_puzzle(puzzle):

    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            number = puzzle[row][col]
            if number == 0:
                for n in range(1, 10):
                    # check every possible value
                    if check_position(puzzle, row, col, n):
                        puzzle[row][col] = n
                        solve_puzzle(puzzle)

                # un-doing the mistake
                puzzle[row][col] = 0
                return

    sudoku.display_puzzle(puzzle)
    exit()


puzzles = []
for puzzle_string in sudoku.read_puzzle_file("puzzles.txt"):
    puzzle = sudoku.process_puzzle_string(puzzle_string)
    puzzles.append(puzzle)


puzzle = puzzles[0]
sudoku.display_puzzle(puzzle)
solve_puzzle(puzzle)
