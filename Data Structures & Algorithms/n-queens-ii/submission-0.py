class Solution:
    def totalNQueens(self, n: int) -> int:
        res=0
        col= set()
        posdiag= set()
        negdiag= set()

        def backtracking(r):
            nonlocal res #Reassigning a variable → nonlocal (or global) needed.
            if r==n:
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
        
                backtracking(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)

        backtracking(0)
        return res