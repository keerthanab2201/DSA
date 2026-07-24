class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        arr=[]
        def dfs(i, total):
            if total==target:
                res.append(arr.copy())
                return
            if i>=len(nums) or total>target:
                return
            arr.append(nums[i])
            dfs(i, total+nums[i])
            arr.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res

            
        