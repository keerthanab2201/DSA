class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window- variable size
        l=0
        sum=0
        minlen=float('inf')
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                minlen= min(minlen, r-l+1)
                sum-=nums[l]
                l+=1
        if minlen==float('inf'):
            return 0
        return minlen


        