class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # use dfs
        rows= len(grid)
        cols= len(grid[0])
        visited= set()

        def dfs(r,c):
            # check left, right, up, down of each cell
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0: 
                return 1 # adds 1 to perimeter
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            perimeter= dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            return perimeter

        # we have to find a land cell to start dfs first
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0: 
                    return dfs(i,j) # "return" stops the for loop here. dfs should be called only once
        return 0 
