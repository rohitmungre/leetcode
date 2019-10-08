class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
        	return 0
        
        tmp_lls = []
        max_len = 0
        for i in range(0, len(s)):
            if i ==0:
                tmp_lls.append(s[0])
            elif s[i] not in tmp_lls[i-1]:
                tmp_lls.append(tmp_lls[i-1]+s[i])
            else:
                #Check accurate format 
                tmp_idx = self.find(s[i], tmp_lls[i-1]) 
                tmp_lls.append(tmp_lls[i-1][tmp_idx+1:] + s[i])
            if len(tmp_lls[i])> max_len:
            	max_len = len(tmp_lls[i])
        return max_len
        
    def find(self, substr, s):
    	for i in range(0, len(s)):
    		if substr == s[i]:
    			return i
    			
    	return -1
