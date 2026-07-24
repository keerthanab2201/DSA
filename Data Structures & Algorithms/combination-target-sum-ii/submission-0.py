class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # now the duplicate elements will be consecutive
        res=[]
        arr=[]
        def dfs(i, total):
            if total==target:
                res.append(arr.copy())
                return
            if i>=len(candidates) or total>target:
                return
            arr.append(candidates[i])
            dfs(i+1, total+candidates[i])
            arr.pop()
            # after popping we want to skip all duplicates
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, total)
        dfs(0,0)
        return res
