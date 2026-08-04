class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        arr=[]
        pick= [False]*len(nums)
        def dfs():
            if len(arr)==len(nums):
                res.append(arr.copy())
                return
            for i in range(len(nums)):
                if pick[i]==False:
                    if i>0 and nums[i]==nums[i-1] and pick[i-1]==False:
                        continue
                    arr.append(nums[i])
                    pick[i]=True
                    dfs()
                    arr.pop()
                    pick[i]=False
        dfs()
        return res
        