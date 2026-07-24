class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min element is first element of rotated portion
        l= 0
        r= len(nums)-1
        while l<r:
            mid= l+(r-l)//2
            if nums[mid]<nums[r]: #sorted portion
                r=mid
            else:
                l=mid+1
        return nums[l]