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



def solveSudoku_2(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
        boxes = [{} for _ in range(9)]
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
 
    def getBox(row,col):
        new_c = col //3
        new_r = (row//3)*3
        return new_c + new_r
 
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                value = board[i][j]
                x = getBox(i,j)
                boxes[x][value]=True
                rows[i][value]=True
                cols[j][value]=True
 
    def isValid(box,row,col,num):
        if (num in box) or (num in row) or (num in col):
            return False
        return True    
 
    def solveBacktrack(board,boxes,rows,cols,r,c):
        if r==9 :
            return True 
        if board[r][c]=='.':
            box = getBox(r,c)
            for num in range(1,10):
                numVal = str(num)
                boxId = getBox(r,c)
                box = boxes[boxId]
                row = rows[r]
                col=cols[c]
                if (isValid(box,row,col,numVal)):
                    board[r][c]= numVal
                    box[numVal]=True
                    row[numVal]=True
                    col[numVal]=True
                    if c==8:
                        if(solveBacktrack(board,boxes,rows,cols,r+1,0)):return True
                    else:
                        if(solveBacktrack(board,boxes,rows,cols,r,c+1)):return True    
                    #backtrack
                    del box[numVal]
                    del row[numVal]
                    del col[numVal]
                    board[r][c]='.'
            return False
        else:
            if c==8:
                if(solveBacktrack(board,boxes,rows,cols,r+1,0)):return True
            else:
                if(solveBacktrack(board,boxes,rows,cols,r,c+1)):return True
 
    solveBacktrack(board,boxes,rows,cols,0,0)



