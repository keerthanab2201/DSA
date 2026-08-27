class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #We need to split the numbers into two groups having equal sum
        # pick some numbers whose sum is target= totalsum/2
        # dp[j]=True if we can form sum j using some of the numbers so far
        # update dp from right to left so each number is used only once
        total= sum(nums)
        if total%2==1:
            return False
        target= total//2
        dp= [False]*(target+1)
        dp[0]=True #sum 0 is always acheivable
        for i in nums:
            for j in range(target,i-1,-1):
                dp[j]= dp[j] or dp[j-i]
        return dp[target]