class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        visited= set()
        maxarea=0
        area=0

        def dfs(r,c):
            # base case
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxarea= max(dfs(i,j),maxarea)
        return maxarea

            