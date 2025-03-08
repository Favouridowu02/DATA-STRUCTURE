#!/usr/bin/python3
"""
    This Module is contains a function that is used to solve a sudoku
    board using backtracking
"""


def solveSudoku(board):
    """
        This Function is used to solve a sudoku board using backtracking.
        The Function modifies the board in place to present the solution. hence there is no need to return the board

        Time Complexity: O(9^(no of empty cells)) = O(1)
        Space Complexity: O(9 * 9) = O(1)
        Arguments:
            board: An arrary of arrays of integers
        Return
    """
    def isValid(board, num, row, col):
        num = int(num) 
        for x in range(9):
            # column check
            if board[x][col] == num:
                return False
            # Row check
            if board[row][x] == num:
                return False
            # box check
            r = 3*(row//3)+x//3
            c = 3*(col//3)+x%3
            if board[r][c]==num:
                return False
        return True


    def fillTheBoard(board):
        for row in range(9):
            for col in range(9):
                if board[row][col]=='.':
                    for num in '123456789':
                        if isValid(board, num, row, col):
                            board[row][col] = num
                            if (fillTheBoard(board)): return True
                            board[row][col] = '.' # backtracking
                    return False

        return True

    fillTheBoard(board)
