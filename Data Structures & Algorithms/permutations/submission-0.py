class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # In permutations, you are not deciding whether to take an element. You're deciding which unused element to place next.
        # we do not skip anything
        res=[]
        perm=[]
        pick= [False]*len(nums) #array to mark which elements are already used
        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if pick[i]==False:
                    perm.append(nums[i])
                    pick[i]=True
                    dfs()
                    perm.pop()
                    pick[i]=False
        dfs()
        return res