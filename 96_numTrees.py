class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <=1:
            return 1
        
        return self.nt_dp(n, {})
    
    def nt_dp(self,n,memo):
        if n in memo:
            return memo[n]
        if n <=1:
            memo[n]=1
            return 1
        lis = [i for i in range(1,n+1)]
        num = 0
        for i in lis:
            num = num + self.nt_dp(i-1, memo)*self.nt_dp(n-i, memo)
        memo[n] = num
        return num



