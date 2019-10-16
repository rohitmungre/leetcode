class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.longest_palindromic_subsequence_dp(s, 0, len(s)-1, {})        
        
    def longest_palindromic_subsequence_dp(self, mystr, sidx, eidx, memo):
        mstr = str(sidx) + '~' + str(eidx)
        if mstr in memo:
            return memo[mstr]
        
        if eidx < 0 or (sidx > eidx) or (sidx>=len(mystr)): 
            memo[mstr] = 0
            return 0

        if sidx == eidx: 
            memo[mstr] = 1
            return 1

        if mystr[sidx] == mystr[eidx]:
            memo[mstr] = 2 + self.longest_palindromic_subsequence_dp(mystr, sidx+1, eidx-1, memo)
            return memo[mstr]

        s1 = self.longest_palindromic_subsequence_dp(mystr, sidx, eidx-1, memo)
        s2 = self.longest_palindromic_subsequence_dp(mystr, sidx + 1, eidx, memo)
        s3 = self.longest_palindromic_subsequence_dp(mystr, sidx + 1, eidx-1, memo)

        memo[mstr] = max(s1, s2, s3)
        return memo[mstr]
