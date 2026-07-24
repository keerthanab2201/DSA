class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=[] #all XOR totals of subsets
        def dfs(i, total):
            if i==len(nums):
                res.append(total)
                return
            dfs(i+1, total^nums[i])
            dfs(i+1, total)
        dfs(0,0)
        return sum(res)
