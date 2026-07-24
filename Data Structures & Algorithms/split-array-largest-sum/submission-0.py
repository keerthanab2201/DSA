class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums) #lower bound
        r=sum(nums) #upper bound
        while l<=r:
            mid= l+(r-l)//2
            sumofsubarray=0
            subarrays=0
            for i in nums:
                if sumofsubarray+i>mid:
                    subarrays+=1
                    sumofsubarray=i
                else:
                    sumofsubarray+=i
            if subarrays<k:
                r=mid-1
            else:
                l=mid+1
        return l


        