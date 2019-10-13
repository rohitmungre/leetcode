class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) < 1:
            return 0
        return self.up_dp(obstacleGrid, 0, 0, {})
        
    def up_dp(self, grid, ridx, cidx, memo):
        mstr = str(ridx) + '~' + str(cidx)
        if mstr in memo:
            return memo[mstr]
        
        if ridx == len(grid)-1 and cidx == len(grid[0])-1:
            if grid[ridx][cidx] == 0:                
                memo[mstr] = 1
                return 1
            else:
                memo[mstr] = 0
                return 0
            
        if grid[ridx][cidx] == 1:
            memo[mstr] = 0
            return 0
        
        if ridx == len(grid)-1:
            memo[mstr] = self.up_dp(grid, ridx, cidx + 1, memo)
            return memo[mstr]
        
        if cidx == len(grid[0])-1:
            memo[mstr] = self.up_dp(grid, ridx+1, cidx, memo)
            return memo[mstr]
        
        p1 = self.up_dp(grid, ridx, cidx + 1, memo)
        p2 = self.up_dp(grid, ridx+1, cidx, memo)
        memo[mstr] = p1+p2        
        return p1 + p2
