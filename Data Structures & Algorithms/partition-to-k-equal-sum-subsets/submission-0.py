class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # approach is exactly like the matchsticks to square problem
        if sum(nums)%k!=0:
            return False
        nums.sort(reverse=True)
        target= sum(nums)//k
        if nums[0]>target:
            return False

        buckets= [0]*k # stores current sum of numbers in each bucket
        # For each number, ask: Which of the k buckets should I put this number into?
        def backtrack(i):
            if i==len(nums): # base case- if every number has been assigned
                return True
            for j in range(k): # loop through choices (buckets)
                if buckets[j]+nums[i]<=target:
                    buckets[j]+=nums[i] # choose
                    if backtrack(i+1): #recurse 
                        return True
                    buckets[j]-=nums[i] #undo
                if buckets[j]==0: #empty buckets are equivalent
                    break
            return False
        return backtrack(0)


            
