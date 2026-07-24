class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        arr=[]
        def dfs(i, count):
            if count==k:
                res.append(arr.copy())
                return
            if i>n:
                return
            arr.append(i)
            dfs(i+1,count+1)
            arr.pop()
            dfs(i+1,count)
        dfs(1,0)
        return res