class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        # dp[i][j] is no of ways to reach (i,j)- left and above
        for i in range(0,m):
            for j in range(0,n):
                if i>0:
                    dp[i][j]+= dp[i-1][j]
                if j>0:
                    dp[i][j]+= dp[i][j-1]
        return dp[m-1][n-1]