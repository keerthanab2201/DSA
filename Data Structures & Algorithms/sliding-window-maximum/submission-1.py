class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        res=[float('-inf')]*(len(nums)-k+1)
        for l in range(len(nums)-k+1):
            r=l
            while r<l+k:
                res[l]=max(res[l],nums[r])
                r+=1
        return res
        