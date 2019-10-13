class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)<1:
            return 0
        if len(triangle[0])<1:
            return 0
        return self.mt_dp(triangle,0,0, {})
        
    def mt_dp(self,triangle, ridx, cidx,memo):
        mstr = str(ridx)+'~'+str(cidx)
        if mstr in memo:
            return memo[mstr]
        
        if ridx == len(triangle)-1:
            memo[mstr] = triangle[ridx][cidx]
            return triangle[ridx][cidx]
        
        s1 = self.mt_dp(triangle, ridx+1, cidx, memo)
        s2 = self.mt_dp(triangle, ridx+1, cidx+1, memo)        
        s = min(s1,s2)
        memo[mstr] = s+triangle[ridx][cidx]
        return s+triangle[ridx][cidx]
