class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        st = ''
        for i in range(n):
            st = st + str(i+1)
        if k > self.factorial(n):
            return st
                   
        res = self.gp(n,k,st)
        return res
        
    def gp(self, n, k, st):
        if len(st) == 1:
            return st
        if len(st) == 2:
            if k == 1:
                return st
            else:
                return st[1]+st[0]
        
        k1 = (k-1)/(self.factorial(n-1)) 
        lst = list(st)
        st_k1 = lst.pop(k1)    
        st = ''.join(lst)
        st_rem = self.gp(n-1, k%(self.factorial(n-1)), st)        
        return st_k1+st_rem
    
    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        return n * self.factorial(n-1)
