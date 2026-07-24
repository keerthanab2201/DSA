class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #approach is to first sort elements, then fix one number i and use two pointer l and r
        res=[] #list can have multiple triplets- dont return directly
        nums.sort() 
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1 #start from here since i is smallest element of that triplet
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]==-nums[i]:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    # skip duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l]+nums[r]<-nums[i]:
                    l+=1
                else:
                    r-=1
        return res
                    
