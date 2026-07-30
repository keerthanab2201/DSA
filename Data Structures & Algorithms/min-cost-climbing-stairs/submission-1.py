class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp= [0]*(len(cost)) # array stores min cost to REACH step i
        # base case- we can start from either 0 or 1
        dp[0]= cost[0]
        dp[1]= cost[1]
        # we can reach stair i from i-1 or i-2
        for i in range(2, len(cost)):
            dp[i]= cost[i]+ min(dp[i-1],dp[i-2])
        return min(dp[len(cost)-1],dp[len(cost)-2])
