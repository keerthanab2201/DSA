class Solution:
    def mySqrt(self, x: int) -> int:
        # find largest integer whose square is atmost x
        l=0
        r=x
        while l<=r:
            mid= l+(r-l)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                l=mid+1
                res=mid
            else:
                r=mid-1
        return res

