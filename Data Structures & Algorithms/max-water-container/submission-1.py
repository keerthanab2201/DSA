class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' approach- we want to find two bars which give maximum area
        area= height*width
        height of bars is given- we take min of the two heights
        width is distance between the two bars

        how do we know which to move?l or r? 
        whichever has smaller height is impeding the max area- so move that pointer

        '''
        i=0
        j=len(heights)-1
        max_area=0
        while i<j:
            area= min(heights[i],heights[j])*(j-i)
            max_area= max(area, max_area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_area
