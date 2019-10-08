class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """        
        p_arr = []
        for i in range(0, len(s)):
            if i == 0:
                p_arr.append(s[0])
            elif i == 1:
                if s[i] == s[i-1]:
                    p_arr.append(s[0:2])
                else:
                    p_arr.append(s[1])
            elif len(p_arr[i-1]) == 1:
                if s[i] == s[i-2]:
                    p_arr.append(s[i-2:i+1])
                elif s[i] == s[i-1]:
                    p_arr.append(s[i-1]+s[i])
                else:
                    p_arr.append(s[i])
            elif s[i] == s[i-len(p_arr[i-1])-1] and len(p_arr[i-1]) != i :
                p_arr.append(s[i-len(p_arr[i-1])-1:i+1])
            else:
                flag = True
                j = i - len(p_arr[i-1])
                while flag:
                    tmp_str = s[j:i+1]
                    if self.is_palindrome(tmp_str):
                        p_arr.append(tmp_str)
                        flag = False
                    j = j+1

        max_lp = ''    
        for i in range(0,len(s)):
            if len(p_arr[i])>len(max_lp):
                max_lp = p_arr[i]                
        return max_lp
                            
    def is_palindrome(self, s):
    	if len(s) == 1:
    		return True
    	if len(s) == 2: 
    		if s[0] == s[1]:
    			return True
    		else:
    			return False
        for i in range(0, len(s)/2 ):
            if s[i] != s[-i-1]:
                return False
        return True
                
