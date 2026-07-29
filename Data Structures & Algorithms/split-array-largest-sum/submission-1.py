class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ''' solution is exactly same as capacity to ship packages within D days
        We find lower and upper bound of the required result variable- assign to l and r to perform binary search
        During binary search, Iterate through the given array and compute the value for given other variable
        Compare with the given variable and increment/decrement accordingly.
        ''' 
        l=max(nums) #lower bound
        r=sum(nums) #upper bound
        while l<=r:
            mid= l+(r-l)//2
            sumofsubarray=0
            subarrays=0
            for i in nums: # split the array so that every subarray has sum ≤ mid
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
