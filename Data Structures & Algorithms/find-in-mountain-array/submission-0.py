class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l=0
        r= mountainArr.length()-1
        # binary search to find the peak
        while l<=r:
            m= l+(r-l)//2
            left= mountainArr.get(m-1)
            mid= mountainArr.get(m)
            right= mountainArr.get(m+1)
            if left<mid<right: 
                l=m+1
            elif left>mid>right:
                r=m-1
            else:
                break
        peak=m

        #binary search left portion of mountain
        l=0
        r=peak-1
        while l<=r:
            m=l+(r-l)//2
            val= mountainArr.get(m)
            if val==target:
                return m
            elif val<target:
                l=m+1
            else:
                r=m-1
            
        #binary search right portion of mountain
        l=peak
        r=mountainArr.length()-1
        while l<=r:
            m=l+(r-l)//2
            val= mountainArr.get(m)
            if val==target:
                return m
            elif val<target:
                r=m-1
            else:
                l=m+1
        
        return -1



        