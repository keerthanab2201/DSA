class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(i:int, j:int) -> bool:
            while i<j:
                if s[i].lower()!=s[j].lower():
                    return False
                i+=1
                j-=1
            return True
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return ispalindrome(l+1,r) or ispalindrome(l,r-1)
            l+=1
            r-=1
        return True
        