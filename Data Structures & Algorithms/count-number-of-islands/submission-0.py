class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
        def dfs(row, col):
            if grid[row][col] == "1":
                grid[row][col] = "0"
                for direction in directions:
                    if (row + direction[0] < 0 or row + direction[0] >= len(grid)
                    or col + direction[1] < 0 or col + direction[1] >= len(grid[0])):
                        continue
                    dfs(row + direction[0], col + direction[1])
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        sol = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    sol += 1
        return sol



        
 
                