class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*(len(nums)+1) #Every element by itself is an increasing subsequence of length 1
        # dp[i] = length of the longest increasing subsequence that ENDS at index i
        for i in range(len(nums)):
            for j in range(i): #check every dp[j] before i since overall LIS doesn't necessarily end at the last element
                if nums[j]<nums[i]:
                    dp[i]= max(dp[i],dp[j]+1)
        return max(dp)

