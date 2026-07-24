class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''rows= len(matrix)
        cols= len(matrix[0])
        l=0
        r=rows*cols-1
        while l<=r:
            mid= l+(r-l)//2
            # flatten the matrix- 2d to 1d
            row=mid//cols
            col=mid%cols
            value= matrix[row][col]
            if value==target:
                return True
            elif value<target:
                l=mid+1
            else:
                r=mid-1
        return False '''

        l=0
        r=len(matrix)-1
        res=-1 #imp
        while l<=r:
            mid=l+(r-l)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                l=mid+1
                res=mid
            else:
                r=mid-1
        if res==-1:
            return False
        i=0
        j=len(matrix[0])-1
        while i<=j:
            mid= i+(j-i)//2
            if matrix[res][mid]==target:
                return True
            elif matrix[res][mid]<target:
                i=mid+1
            else:
                j=mid-1
        return False
