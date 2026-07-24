class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # we can use two pointers since array is sorted- start at ends and decrement by removing elements farther frm x until only k remain
        l=0
        r= len(arr)-1
        while r-l>=k:
            if abs(x-arr[l])<=abs(x-arr[r]): #remove element that is farther away
                r-=1
            else:
                l+=1
        return arr[l:r+1]


        

        
        
        


        