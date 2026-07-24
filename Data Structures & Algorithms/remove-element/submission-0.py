class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i= len(nums)-1
        j= len(nums)-1
        k=0
        while i>=0:
            if nums[i]==val:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
                i-=1
            else:
                k+=1
                i-=1   
        return k