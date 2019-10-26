class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return words
        
        res = []
        for item in words: 
            if self.belongsToSameRow(item):
                res.append(item)                
        return res 
    
    def belongsToSameRow(self, word):
        if len(word) == 0:
            return True
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'

        row = ''
        if str(word[0]).lower() in row1:
            row = row1
        elif str(word[0]).lower() in row2:
            row = row2
        else:
            row = row3
        for char in word:
            if str(char).lower() not in row:
                return False            
        return True
