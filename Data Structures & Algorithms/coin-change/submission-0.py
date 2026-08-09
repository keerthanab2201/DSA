class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1) #stores minimum coins needed to make an amount- initialise with large value
        dp[0]=0
        for c in coins:
            for i in range(c, amount+1):
                dp[i]= min(dp[i], dp[i-c]+1)
        return -1 if dp[amount]==float('inf') else dp[amount]
