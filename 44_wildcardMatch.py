class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.wc_matching_dp(s, p,0,0, {})
        
    def wc_matching_dp(self, st, wc, sidx, widx,memo):
        mstr = str(sidx)+'~'+str(widx)
        if mstr in memo:
            return memo[mstr]
        
        if sidx == len(st) and widx == len(wc):
                memo[mstr] = True
                return memo[mstr]
        
        if sidx == len(st):
            if wc[widx] == '*':
                memo[mstr] = self.wc_matching_dp(st,wc,sidx,widx+1,memo)
                return memo[mstr]
            else:
                memo[mstr] = False
                return memo[mstr]
            
        if widx >= len(wc):
            memo[mstr] = False
            return memo[mstr]
        
        if st[sidx] == wc[widx] or wc[widx] == '?':
            memo[mstr] = self.wc_matching_dp(st,wc,sidx+1,widx+1,memo)
            return memo[mstr]
                
        if wc[widx] == '*':
            memo[mstr] = self.wc_matching_dp(st,wc,sidx+1,widx,memo) or self.wc_matching_dp(st,wc,sidx+1,widx+1,memo) or self.wc_matching_dp(st, wc, sidx, widx+1, memo)
            return memo[mstr]

        memo[mstr] = False
        return memo[mstr]
