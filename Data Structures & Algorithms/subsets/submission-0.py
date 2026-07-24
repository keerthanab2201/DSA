class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i==len(nums): #base case- we have reached leaf node- Every number has either been included or excluded.
                res.append(subset.copy()) #Later, when subset changes, every entry in res should not change too.
                return #This path is finished. Go back to the previous decision.
            subset.append(nums[i]) #we can either append the number and recursively explore
            dfs(i+1)
            subset.pop() # or we can pop the number and recursively explore
            dfs(i+1)
        dfs(0)
        return res