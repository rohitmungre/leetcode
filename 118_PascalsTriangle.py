class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(2,numRows+1):
            row = [0 for j in range(i)]
            row[0]=1
            row[-1]=1
            for ii in range(1,i-1):
                row[ii] = res[i-2][ii-1]+res[i-2][ii]            
            res.append(row)
            
        return res
