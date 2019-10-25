class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if len(S)<1 or len(J)<1:
            return 0
        
        count = 0
        for char in list(S):
            if char in J:
                count = count+1
                
        return count 
