class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # no need to find minimum element- perform one modified binary search
        # since we dont know the rotation point/minimum element, at any point in the array- one half of array is guaranteed to be sorted
        l=0
        r= len(nums)-1
        while l<=r:
            m= l+(r-l)//2
            if nums[m]==target:
                return True
            if nums[l]<nums[m]: #left portion is sorted
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            elif nums[m]<nums[l]: #right portion is sorted
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            else: #nums[l]=nums[m] i.e. duplicates but we do not know anything about the elements in between them
                l+=1
        return False