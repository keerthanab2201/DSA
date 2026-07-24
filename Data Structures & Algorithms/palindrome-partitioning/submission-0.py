class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        palindrome=[]

        def isValidPalindrome (string, i , j)->bool:
            while i<j:
                if string[i]!=string[j]:
                    return False
                i+=1
                j-=1
            return True

        def backtracking(i):
            if i>=len(s):
                res.append(palindrome.copy())
                return
            for j in range(i,len(s)): # this loop chooses where the current palindrome should end 
                if isValidPalindrome(s, i, j):
                    palindrome.append(s[i:j+1])
                    backtracking(j+1) #How should I partition the REST of the string?
                    palindrome.pop() 
        backtracking(0)
        return res

        

