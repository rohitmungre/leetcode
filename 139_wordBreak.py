class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        return self.word_break_dp(s, wordDict, {})
        
        
    def word_break_dp(self, st, di, memo):    
        if st in memo: 
            return memo[st]

        if len(st) == 0: 
            return True

        res = False
        for item in di: 
            if st.startswith(item):
                temp, nst = st.split(item,1)
                res = self.word_break_dp(nst, di, memo)
                if res == True:
                    return res
        memo[st] = res
        return res
