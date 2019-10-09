class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n<=0:
            return []
        if n<k:
            return []
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in range(1,n+1)]
        c1 = self.combine(n-1,k-1)
        for i in range(0,len(c1)):
            c1[i] = c1[i]+[n]
        c2 = self.combine(n-1,k)
        
        return c1+c2
