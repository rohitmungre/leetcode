class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<1 and n<1:
            return 0
        if m <1 or n<1:
            return 1
        return self.up_dp(0,0,m-1,n-1,{})
        
    def up_dp(self, i, j , m, n, memo):
        mstr = str(i) + '~' + str(j)
        if mstr in memo:
            return memo[mstr]
        
        if i == m and j == n :
            memo[mstr] = 1
            return 1

        if i == m :
            memo[mstr] = 1
            return 1
        
        if j == n:
            memo[mstr] = 1
            return 1
        
        p1 = self.up_dp(i+1,j,m,n,memo)
        p2 = self.up_dp(i,j+1,m,n,memo)
        memo[mstr]=p1+p2
        return p1+p2
