class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min element is first element of rotated portion
        l=0
        r=len(nums)-1
        while l<r:
            m= l+(r-l)//2
            if nums[m]<nums[r]: #sorted portion
                r=m
            else:
                l=m+1
        return nums[l]
        

    