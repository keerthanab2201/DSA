class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes algorithm
        globalmax= nums[0]
        curmax= 0
        for i in nums:
            curmax= max(i,curmax+i) # we can either start a new subarray or increment the same
            globalmax= max(curmax,globalmax)
        return globalmax

        