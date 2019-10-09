class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def validate(mat):
            uitems = []
            for i in range(0, len(mat)):
                for j in range(0, len(mat[0])):
                    if mat[i][j] in uitems and mat[i][j] != '.':
                        return False
                    uitems.append(mat[i][j])
            return True
        
        #rows
        for row in board:
            if validate(row) == False:
                return False
            
        #cols
        for j in range(0, len(board[0])):
            col = [board[i][j] for i in range(0, len(board))]
            if validate(col) == False:
                return False

        #sub-boxes 
        for i in range(0,3):
            for j in range(0,3):
                subbox = [[board[(3*i)+z][(3*j)+y] for y in range(0,3)] for z in range(0,3)]
                if validate(subbox) == False:
                    return False
        
        return True
