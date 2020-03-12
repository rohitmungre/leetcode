import copy
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        counter = 0
        if len(grid) == 0:
            return counter          
        marked_grid = [[str(x) for x in item] for item in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if str(marked_grid[i][j]) == '1':
                    counter -= 1                     
                    self.mark_the_grid(marked_grid, i, j, counter) 
        return counter*-1
    
    def mark_the_grid(self, marked_grid, i , j, counter):
        marked_grid[i][j]=counter
        if i < len(marked_grid)-1:
            if marked_grid[i+1][j] == '1':
                self.mark_the_grid(marked_grid, i+1, j, counter)
        if j < len(marked_grid[0])-1:
            if marked_grid[i][j+1] == '1':
                self.mark_the_grid(marked_grid, i, j+1, counter)
        if i > 0:
            if marked_grid[i-1][j] == '1':
                self.mark_the_grid(marked_grid, i-1, j, counter)
        if j > 0:
            if marked_grid[i][j-1] == '1':
                self.mark_the_grid(marked_grid, i, j-1, counter)
        
