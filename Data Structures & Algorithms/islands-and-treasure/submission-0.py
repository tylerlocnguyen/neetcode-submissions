from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 0:
                        q.append([i,j])
                        visit.add((i,j))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                

                for direction in directions:
                    if r + direction[0] < 0 or r + direction[0] >= rows or c + direction[1] < 0 or c + direction[1] >= cols or (r + direction[0], c + direction[1]) in visit or grid[r + direction[0]][c + direction[1]] == -1:
                        continue
                    q.append([r + direction[0], c + direction[1]])
                    visit.add((r + direction[0],c + direction[1]))
            distance += 1








        