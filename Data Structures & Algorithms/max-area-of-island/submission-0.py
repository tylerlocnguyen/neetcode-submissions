class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        sol = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(row, col):
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            curr = 1
            for direction in directions:
                if (row + direction[0] < 0 or row + direction[0] >= rows
                    or col + direction[1] < 0 or col + direction[1] >= cols):
                        continue
                curr += dfs(row + direction[0], col + direction[1])
            return curr
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    sol = max(area, sol)
        

        return sol
                




        