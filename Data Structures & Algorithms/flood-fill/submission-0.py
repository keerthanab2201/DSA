class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:        
        # dfs solution
        origcolor= image[sr][sc]
        if origcolor==color:
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c]!=origcolor:
                return
            image[r][c]= color
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        dfs(sr,sc)
        return image

