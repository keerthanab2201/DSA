class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointer approach- expand symmetrically from the middle
        # we need to handle both odd and even length palindromes
        res= ""

        def helper(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(len(s)):
        #IMP- check for both odd and even length palindromes
            odd= helper(i,i)
            even= helper(i,i+1)
            if len(odd)>len(res):
                res= odd
            if len(even)>len(res):
                res= even
        return res