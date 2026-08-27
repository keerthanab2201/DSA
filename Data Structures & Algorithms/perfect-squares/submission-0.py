class Solution:
    def numSquares(self, n: int) -> int:
        dp= [n]*(n+1)
        dp[0]=0
        for sum in range(1,n+1):
            for num in range(1,sum+1):
                if num*num<=sum:
                    dp[sum]= min(dp[sum],1+dp[sum-num*num])
        return dp[n]
