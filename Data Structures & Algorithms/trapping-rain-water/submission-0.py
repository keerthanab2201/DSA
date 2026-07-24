class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        for i in range(len(height)):
            # initialise two arrays- these will store left max and right max of each height element
            leftmax= rightmax= height[i]
            for j in range(i):
                leftmax= max(leftmax, height[j])
            for j in range(i+1,len(height)):
                rightmax= max(rightmax, height[j])
            area+= min(leftmax,rightmax)-height[i]
        return area