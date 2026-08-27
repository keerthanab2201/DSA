class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m= len(obstacleGrid)
        n= len(obstacleGrid[0])
        # check for start and end obstacles first
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i>0 and obstacleGrid[i][j]==0:
                    dp[i][j]+= dp[i-1][j]
                if j>0 and obstacleGrid[i][j]==0:
                    dp[i][j]+= dp[i][j-1]
        return dp[m-1][n-1]