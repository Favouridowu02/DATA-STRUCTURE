def solveSudoku(board):
    #The function modifies the board in place to present the solution. Hence there is no need to return the board 

    def isValid(board, row, col, num):
        # Check if a number 'num' can be placed at board[row][col].
        for x in range(9):
            # Check row and column: The number must not already exist in the same row and column.
            if board[x][col] == num or board[row][x] == num:
                return False

            # Calculate the start row and column index for the 3x3 sub-box.
            r = 3 * (row // 3) + x // 3
            c = 3 * (col // 3) + x % 3

            # Check 3x3 sub-box: The number must not already exist in the same 3x3 sub-box.
            if board[r][c] == num:
                return False

        # If the number 'num' is not found in the same row, column, and 3x3 sub-box, it is valid.
        return True

    def helper(board):
        # Iterate through each cell in the board.
        for row in range(9):
            for col in range(9):
                # If the cell is empty ('.').
                if board[row][col] == '.':
                    # Try placing each number from 1 to 9 in the empty cell.
                    for num in '123456789':
                        # Check if the number is valid in the current position.
                        if isValid(board, row, col, num):
                            # Place the number in the cell.
                            board[row][col] = num

                            # Recursively attempt to solve the rest of the board with this number placed.
                            if helper(board):
                                return True

                            # If placing the number does not lead to a solution, reset the cell and try the next number.
                            board[row][col] = '.'

                    # If no number from 1 to 9 can be placed in this cell, backtrack.
                    return False

        # If the entire board is filled without conflicts, the puzzle is solved.
        return True

    # Start the solving process.
    helper(board)

    
    

