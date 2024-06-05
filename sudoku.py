def is_valid_move(board, row, col, num):
    # Check if the number is already in the row
    if num in board[row]:
        return False
    
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is already in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    # If there are no empty locations left, the Sudoku is solved
    if row is None:
        return True
    
    # Try placing numbers from 1 to 9
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            
            # Recursively try to solve the Sudoku
            if solve_sudoku(board):
                return True
            
            # If we reach here, the current placement didn't lead to a solution
            # So, we backtrack
            board[row][col] = 0
    
    # If no number fits, return False to backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Example Sudoku puzzle
input_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Copy the input grid to avoid modifying the original
board = [row[:] for row in input_grid]

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("Sudoku Solved Successfully:")
    print_board(board)
else:
    print("No solution exists.")
