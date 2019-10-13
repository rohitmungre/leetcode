import copy
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word)<1:
            return False
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                res = self.xst(board,word,i,j,[])
                if res == True:
                    return True
        return False
        
    def xst(self, board, word, ridx, cidx, path):
        if len(word) == 1:
            if board[ridx][cidx] == word:
                return True
            return False
        if board[ridx][cidx] == word[0]:
            ls = list(word)
            cword = ''.join(ls[1:])
            path.append([ridx,cidx])            
            if ridx != 0 and [ridx-1 ,cidx] not in path:
                res = self.xst(board, cword, ridx-1, cidx, path)
                if res == True:
                    return True
            if cidx != 0 and [ridx ,cidx-1] not in path:
                res = self.xst(board, cword, ridx, cidx-1, path)
                if res == True:
                    return True
            if ridx != len(board)-1 and [ridx+1 ,cidx] not in path:
                res = self.xst(board, cword, ridx+1, cidx, path)
                if res == True:
                    return True
            if cidx != len(board[0])-1 and [ridx ,cidx+1] not in path:
                res = self.xst(board, cword, ridx, cidx+1, path)
                if res == True:
                    return True
            path.remove([ridx, cidx])
        return False        
                
