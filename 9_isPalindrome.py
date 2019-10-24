class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False        
        if x <10:
            return True        
        return self.ip(str(x))
        
    def ip(self,st):
        if len(st)<2:
            return True        
        if st[0] != st[-1]:
            return False
        if len(st) == 2:
            return True
        return self.ip(st[1:-1])
