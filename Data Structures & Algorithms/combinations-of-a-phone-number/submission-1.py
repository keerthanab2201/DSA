class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb=[]
        res=[]
        digittochar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtracking(i):
            if i==len(digits):
                res.append("".join(comb))
                return
            for c in digittochar[digits[i]]:
                comb.append(c)
                backtracking(i+1)
                comb.pop()
        if digits:
            backtracking(0)
        return res