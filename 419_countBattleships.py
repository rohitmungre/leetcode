class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        numShips = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if i == 0:
                    if board[i][j] == 'X':
                        if j == 0:
                            numShips = numShips +1
                        elif board[i][j-1] != 'X':
                            numShips = numShips + 1
                else:
                    if board[i][j] == 'X':
                        if j == 0:
                            if board[i-1][j] != 'X':
                                numShips = numShips + 1
                        else:
                            if board[i][j-1] != 'X' and board[i-1][j] != 'X':
                                    numShips = numShips + 1
                    
        return numShips
