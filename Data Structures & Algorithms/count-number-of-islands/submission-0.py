class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        visited=set()
        islands=0

        def dfs(r,c):
            # base case- if cell is out of bounds or water, recursion stops
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    islands+=1
        return islands

