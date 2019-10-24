class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex < 0:
            return []
        
        if rowIndex == 0:
            return [1]
        prev_row = [1]
        for i in range(2,rowIndex+2):
            row = [0 for j in range(i)]
            row[0]=1
            row[-1]=1
            for ii in range(1,i-1):
                row[ii] = prev_row[ii-1]+prev_row[ii]            
            prev_row = row
            
        return row
