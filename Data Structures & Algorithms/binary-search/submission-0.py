class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(l,r):
            if l>r:
                return -1
            mid= l+ ((r-l)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return binarysearch(mid+1, r)
            else:
                return binarysearch(l, mid-1)
        return binarysearch(0,len(nums)-1)