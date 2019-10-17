class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.cs_dp(n, {})
    
    def cs_dp(self, n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = 1
            return 1
        
        memo[n] = self.cs_dp(n-1,memo) + self.cs_dp(n-2,memo)
        return memo[n]
    
