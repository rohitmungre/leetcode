class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
                
        return self.num_ways_dp(s, 0, {})
    
    def num_ways_dp(self, s, idx, memo):
        if idx in memo:
            return memo[idx]

        if len(s) == 0:
            return 0
            
        if idx == len(s):
            memo[idx] = 1
            return 1
        
        if idx == len(s)-1: 
            if s[idx] == '0':
                memo[idx] = 0
                return 0                
            else:
                memo[idx] = 1
                return 1

        if s[idx]=='1':              
            memo[idx] = self.num_ways_dp(s, idx+1, memo) + self.num_ways_dp(s, idx+2, memo)
            return memo[idx]
        elif s[idx] == '2':
            if s[idx+1] in '0123456':
                memo[idx] = self.num_ways_dp(s, idx+1, memo) + self.num_ways_dp(s, idx+2, memo)
            else:
                memo[idx] = self.num_ways_dp(s, idx+1, memo)
            return memo[idx]        
        elif s[idx] == '0':
            memo[idx] = 0
            return 0
        else:
            memo[idx] = self.num_ways_dp(s, idx+1, memo)
            return memo[idx]
