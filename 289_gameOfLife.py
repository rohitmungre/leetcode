class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        if len(board[0]) == 0:
            return
        original = [[str(x) for x in item] for item in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find_next_state(original, board, i, j)
                
    def find_next_state(self, original, board, i, j):
        count = 0
        
        if i>0:
            if original[i-1][j] == '1':
                count += 1
        if i<len(board)-1:        
            if original[i+1][j] == '1':
                count += 1
        if j>0:
            if original[i][j-1] == '1':
                count += 1
        if j<len(board[0])-1:        
            if original[i][j+1] == '1':
                count += 1
        if i>0 and j>0:
            if original[i-1][j-1] == '1':
                count += 1
        if i<len(board)-1 and j<len(board[0])-1:        
            if original[i+1][j+1] == '1':
                count += 1
        if i>0 and j<len(board[0])-1:        
            if original[i-1][j+1] == '1':
                count += 1
        if i<len(board)-1 and j>0:        
            if original[i+1][j-1] == '1':
                count += 1
        
        if original[i][j] == '1':
            if count not in (2,3):
                board[i][j] = 0
                
        if original[i][j] == '0' and count == 3:
            board[i][j] = 1
            
