class Solution:
    def countSubstrings(self, s: str) -> int:
        res= 0
        def helper(l,r,count):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                count+=1
            return count
        for i in range(len(s)):
            odd= helper(i,i,0)
            even= helper(i,i+1,0)
            res+= odd+even
        return res
