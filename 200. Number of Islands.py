class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # Start dfs
                    count += 1
                    self.dfs(grid, i, j)
        
        return count
    
    def dfs(self,grid, i, j):
        nr = len(grid)
        nc = len(grid[0])
        
        grid[i][j] = '0'
        # search all direction
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1,j)
        if i + 1 < nr and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j)
        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j - 1)
        if j + 1 < nc and grid[i][j+1] == '1':
            self.dfs(grid, i, j + 1)
        
