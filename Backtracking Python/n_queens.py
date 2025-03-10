    def solveNQueens(n):
    """

        Space Complexity: O(n^2)
        Time Complexity: T = O(n!)
    """
    # List of Lists, which will be changed to a list of strings
    res = []
    board = [['.']*n for _ in range(n)]
    def convertBoard(board):
        return [''.join(row) for row in board]
    def isValid(row, col, board):
        # Column check
        for x in range(row):
            if board[x][col] == 'Q': return False
        # Top Left Diagonal Check
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[r][c] == 'Q': return False

        # Top Right diagonal
        for r, c in zip(range(row, -1, -1), range(col, n)):
            if board[r][c] == 'Q': return False
        return True

    def placeNextQueen(board, row):
        # Base case
        if row == n:
            res.append(convertBoard(board))
            return
        for col in range(n):
            if (isValid(row, col, board)):
                board[row][col] = 'Q'
                placeNextQueen(board, row + 1)
                board[row][col] = '.'
    placeNextQueen(board, 0)
    return res