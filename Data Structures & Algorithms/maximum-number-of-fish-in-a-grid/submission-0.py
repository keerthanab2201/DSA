class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        ans=0
        def dfs(r,c): #imp- look at the return values properly in each step
            if r<0 or c<0 or r==rows or c==cols or grid[r][c]==0:
                return 0
            fish= grid[r][c] # collect all the fish in this cell
            grid[r][c]= 0 # mark as visited after collecting so we dont traverse this cell again
            fish+= dfs(r+1,c)
            fish+= dfs(r-1,c)
            fish+= dfs(r,c+1)
            fish+= dfs(r,c-1)
            return fish
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]>0:
                    ans= max(ans,dfs(r,c))
        return ans

