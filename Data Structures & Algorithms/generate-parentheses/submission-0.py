class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # no of open brackets = no of closed brackets = n
        # we can only add a closed bracket when no of closed brackets < open brackets
        res=[]
        array= []
        def backtracking(opened,closed):
            if opened==closed==n:
                res.append("".join(array))
                return
            if opened<n:
                array.append("(")
                backtracking(opened+1,closed)
                array.pop()
            if closed<opened:
                array.append(")")
                backtracking(opened,closed+1)
                array.pop()
        backtracking (0,0)
        return res

        
