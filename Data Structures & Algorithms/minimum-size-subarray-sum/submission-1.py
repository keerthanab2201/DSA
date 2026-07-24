class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window- variable size
        i=0
        minlen=float('inf')
        for i in range(len(nums)):
            j=i
            sum=0
            while j<len(nums):
                sum+=nums[j]
                if sum>=target:
                    minlen= min(minlen, j-i+1)
                    break
                j+=1
        if minlen==float('inf'):
            return 0
        return minlen


        