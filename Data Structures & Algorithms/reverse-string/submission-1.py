class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        m= (l+r)//2
        
        while l<r:
            temp=s[l]
            s[l]=s[r]
            s[r]=temp
            l+=1 
            r-=1
        return s