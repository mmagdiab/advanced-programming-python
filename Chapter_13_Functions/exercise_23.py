"""
Write a function that is given a 9 x 9 potentially solved Sudoku and returns True if it is
solved correctly and False if there is a mistake. The Sudoku is correctly solved if there are
no repeated numbers in any row or any column or in any of the nine “blocks.”
"""

solved_sudoku = [[5, 1, 7, 6, 9, 8, 2, 3, 4],
                 [2, 8, 9, 1, 3, 4, 7, 5, 6],
                 [3, 4, 6, 2, 7, 5, 8, 9, 1],
                 [6, 7, 2, 8, 4, 9, 3, 1, 5],
                 [1, 3, 8, 5, 2, 6, 9, 4, 7],
                 [9, 5, 4, 7, 1, 3, 6, 8, 2],
                 [4, 9, 5, 3, 6, 2, 1, 7, 8],
                 [7, 2, 3, 4, 8, 1, 5, 6, 9],
                 [8, 6, 1, 9, 5, 7, 4, 2, 3]]


def is_solved(sudoku: list):
    # Check for lines
    for i in range(9):
        row_line = []
        colum_line = []
        for j in range(9):
            row_line.append(sudoku[i][j])
            colum_line.append(sudoku[j][i])

        if len(set(row_line)) != len(row_line):
            return False
        if len(set(colum_line)) != len(row_line):
            return False

    # Check boxes
    first_elem_in_box = [[0, 0], [3, 0], [6, 0],
                         [6, 3], [6, 6], [6, 6],
                         [6, 3], [6, 6], [6, 6]]

    for cell in first_elem_in_box:
        row = cell[0] + 3
        column = cell[1] + 3
        for i in range(row):
            box = []
            for j in range(column):
                box.append(sudoku[i][j])
            if len(set(box)) != len(box):
                return False

    return True
