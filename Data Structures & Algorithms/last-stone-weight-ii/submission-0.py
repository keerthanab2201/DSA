class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #Divide the stones into two groups whose sums are as close as possible.
        # difference = total_sum - 2 * sum(A) where sum(A) is the largest subset sum that doesn't exceed total_sum / 2.
        # this is NOT stack since stones can be chosen in any order
        #dp[i][t] represents the maximum sum achievable using the first i stones without exceeding capacity t
        target= sum(stones)//2
        dp=[[0]*(target+1) for _ in range(len(stones)+1)]
        for i in range(1,len(stones)+1):
            for j in range(1,target+1):
                if j>=stones[i-1]:
                    dp[i][j]= max(dp[i-1][j], dp[i-1][j-stones[i-1]]+stones[i-1])
                else:
                    dp[i][j]= dp[i-1][j]
        return sum(stones)- 2*dp[len(stones)][target]