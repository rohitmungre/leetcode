class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<2:
            return s
        c_idx = [0,0]
        s_idx = 0
        
        if numRows<1:
        	return ''
        elif numRows == 1:
        	return s
        else:
	        av_el_col = numRows/(numRows-1)
        numCols = (len(s)/av_el_col)+1
        mat = [['' for i in range(0,numCols)] for j in range(0,numRows)]
        direction = 'down'
        for i in range(0,len(s)):
            mat[c_idx[0]][c_idx[1]] = s[i]
            i = i+1
            if direction == 'down':
                if c_idx[0] == numRows-1:
                    direction = 'up'
                    c_idx[0] = c_idx[0]-1
                    c_idx[1] = c_idx[1]+1
                else:
                    c_idx[0] = c_idx[0] + 1
            elif direction == 'up':
                if c_idx[0] == 0:
                    direction = 'down'
                    c_idx[0] = c_idx[0]+1
                else:
                    c_idx[0] = c_idx[0]-1
                    c_idx[1] = c_idx[1]+1        
        res = ''
        for i in range(0, numRows):
        	tmp = ''.join(mat[i])
        	res = res + tmp
        return res
