class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # none of the queens can share same row or same column or same positive diagonal or same negative diagonal
        res=[]
        board= [["."]*n for i in range(n)] #this is a nxn 2D array filled with "."
        col = set()
        posdiag= set() # all cells in a positive diagonal has same (r+c) value
        negdiag= set() # all cells in a negative diagonal has same (r-c) value
        def backtracking(r):
            if r==n:
                copy = ["".join(row) for row in board] #this joins all the elements in a row
                res.append(copy)
                return
            for c in range(n): # this tries every column in a row
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]= "Q"

                backtracking(r+1) #recurse to next row

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]= "."

        backtracking(0)
        return res

