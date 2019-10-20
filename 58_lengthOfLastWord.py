class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        i = 0
        c = s[-1]        
        while c == ' ' and i < len(s):
            i = i+1
            c = s[-1*(i)]        
        
        j = max(i,1) 
        if i == len(s) and s[-1*i]==' ':
            return 0
        elif i==len(s):
            return 1
        while c != ' ' and i < len(s):
            i = i+1
            c = s[-1*(i)]
        
        if s[-1*i] != ' ':
            i = i+1
        return i-j
            
