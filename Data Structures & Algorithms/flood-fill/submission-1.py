class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:        
        '''# dfs solution
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
        return image'''

        # bfs solution
        origcolor= image[sr][sc]
        if origcolor==color:
            return image
        q= deque([(sr,sc)])
        image[sr][sc]=color
        def func(r,c):
            if r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c]!=origcolor:
                return
            image[r][c]= color
            q.append((r,c))
        while q:
            r,c= q.popleft()
            func(r+1,c)
            func(r-1,c)
            func(r,c+1)
            func(r,c-1)
        return image



