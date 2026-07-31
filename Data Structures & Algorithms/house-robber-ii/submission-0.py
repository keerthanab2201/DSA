class Solution:
    def rob(self, nums: List[int]) -> int:
        '''Since houses are in a circle, you can't rob both first and last house.
            So solve two House Robber I problems:
            Rob houses 0 ... n-2
            Rob houses 1 ... n-1'''
        
        if len(nums) == 1:
            return nums[0]

        def helper(arr):

            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])

            return dp[-1]

        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )