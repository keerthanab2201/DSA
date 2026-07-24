class Solution:
    def trap(self, height: List[int]) -> int:
        area=0 # equal to min(leftmax,rightmax)- height of current
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        #initialise leftmax as first element and rightmax as last element
        #iterate forward to compute leftmax for each element 
        #iterate backward to compute rightmax for each element
        leftmax[0]= height[0]
        rightmax[len(height)-1]= height[len(height)-1]
        for i in range(1,len(height)):
            leftmax[i]= max(leftmax[i-1],height[i])
        for i in range(len(height)-2, -1, -1):
            rightmax[i]= max(rightmax[i+1], height[i])
        for i in range(len(height)):
            area+= min(leftmax[i],rightmax[i])-height[i]
        return area



        