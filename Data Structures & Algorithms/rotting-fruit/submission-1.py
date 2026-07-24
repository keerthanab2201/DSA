class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        rotten= set()
        q= deque()
        fresh=0
        time=0

        def makerot(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or grid[r][c]==2:
                return
            grid[r][c]=2
            q.append((r,c))
            fresh-=1

        for i in range(rows): # queue contains all rotten fruits at time 0 (initial)
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
                    
        while q and fresh>0:
            for rottenfruit in range(len(q)): # one entire for loop processes one bfs level (queue at a given minute)
                r,c= q.popleft()
                #process neightbours of rotten fruits in queue
                makerot(r+1,c)
                makerot(r-1,c)
                makerot(r,c+1)
                makerot(r,c-1)
            time+=1 #imp- time is incremented outside for loop i.e. bfs level+=1
            #queue contains all oranges that are rotten at the current minute
        return time if fresh==0 else -1

