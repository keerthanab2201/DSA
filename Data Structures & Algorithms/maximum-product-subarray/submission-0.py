class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # use kadane's algo- o(n) time- but we track both current min and current max
        res= nums[0]
        curmin=1
        curmax=1
        for i in nums:
            temp= curmax*i
            curmax= max(curmax*i, curmin*i, i)
            curmin= min(temp, curmin*i, i)
            res= max(res, curmax)
        return res