class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # use bfs since we want to find shortest path in unweighted grid
        # From one empty cell (INF), we expand level-by-level (distance 0, 1, 2, ...) to find a treasure cell
        # this guarantees minimum steps needed
        rows= len(grid)
        cols= len(grid[0])
        INF = 2147483647
        visited= set()
        q= deque()

        def addcell(r,c):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visited or grid[r][c]==-1:
                return
            visited.add((r,c))
            q.append([r,c])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0: # if treasure cell
                    q.append([i,j]) # our queue initially has all the treasure cells
                    visited.add((i,j))
        dist=0
        while q:
            for treasure in range(len(q)):
                r,c= q.popleft()
                grid[r][c]=dist
                addcell(r+1,c)
                addcell(r,c+1)
                addcell(r-1,c)
                addcell(r,c-1)
            dist+=1

# read problem- rotting fruit- to understand better- both use same bfs queue logic



