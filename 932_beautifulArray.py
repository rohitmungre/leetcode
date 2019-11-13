class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """        
        return self.ba_dp(N, {})
    
    def ba_dp(self, N, memo):
        if N in memo:
            return memo[N]
        if N == 1:
            memo[N] = [1]
            return [1]
        odds = self.ba_dp((N+1)/2, memo)
        evens = self.ba_dp(N/2, memo)
        
        res = [2*x for x in evens] + [2*x-1 for x in odds]
        memo[N] = res
        return memo[N]
        
        
        
