class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums) # array stores max amt of money robbed till that house
        dp[0]= nums[0]
        dp[1]= max(nums[1],nums[0])
        '''At every house, you have two choices:
        Skip the current house → move to the next house.
        Rob the current house → take its money and skip the next house.
        For each house i, the maximum money we can have depends on:
        Not robbing it → same money as i - 1
        Robbing it → money at i + best up to i - 2'''
        for i in range(2, len(nums)):
            dp[i]= max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]