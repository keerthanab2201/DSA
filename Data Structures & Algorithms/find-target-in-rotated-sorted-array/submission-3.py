class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r= len(nums)-1
        #first find minimum of rotated array using binary search
        while l<r: #l<r stops when exactly one element remains- this is minimum
            m= l+(r-l)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        min=l
        #then search in the 2 halves using binary search again
        l=0
        r=len(nums)-1
        if nums[min]<=target<=nums[r]: #to find the correct half
            l=min
        else:
            r=min-1
        while l<=r: #l<=r checks all elements- use when there is a possibility of not finding the required element
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return -1

    
    