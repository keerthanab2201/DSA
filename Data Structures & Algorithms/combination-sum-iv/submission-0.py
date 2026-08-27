class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 0/1 knapsack
        # dp[j]=no of combinations that add up to sum j
        dp=[0]*(target+1)
        dp[0]=1 
        for sum in range(1,target+1):
            for num in nums:
                if num<=sum:
                    dp[sum]+= dp[sum-num]
        return dp[target]