class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        return self.mps_dp(grid, 0 , 0 , {})
        
    def mps_dp(self, grid, idx_r, idx_c, memo):
        mstr = str(idx_r) + '~' + str(idx_c)
        if mstr in memo:
            return memo[mstr]
        if idx_r == len(grid)-1 and idx_c == len(grid[0])-1:
            memo[mstr] = grid[idx_r][idx_c]
            return grid[idx_r][idx_c]
        
        if idx_r == len(grid) - 1:
            memo[mstr] = grid[idx_r][idx_c] + self.mps_dp(grid, idx_r, idx_c+1, memo)
            return grid[idx_r][idx_c] + self.mps_dp(grid, idx_r, idx_c+1, memo)
        
        if idx_c == len(grid[0])-1:
            memo[mstr] = grid[idx_r][idx_c] + self.mps_dp(grid, idx_r+1, idx_c, memo)
            return grid[idx_r][idx_c] + self.mps_dp(grid, idx_r+1, idx_c, memo)

        s1 = self.mps_dp(grid, idx_r+1, idx_c, memo)
        s2 = self.mps_dp(grid, idx_r, idx_c+1, memo)
        memo[mstr] = min(s1,s2) + grid[idx_r][idx_c]        
        return min(s1,s2) + grid[idx_r][idx_c] 
