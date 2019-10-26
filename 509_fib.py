class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<0:
            return -1*self.fib_dp(-1*N, {})
        return self.fib_dp(N, {})
        
    def fib_dp(self, N, memo):
        if N in memo:
            return memo[N]
            
        if N == 0:
            memo[N] = 0
            return 0
        
        if N == 1:
            memo[N] = 1
            return 1 

        val = self.fib_dp(N-1, memo) + self.fib_dp(N-2, memo)
        memo[N] = val
        return val
        
