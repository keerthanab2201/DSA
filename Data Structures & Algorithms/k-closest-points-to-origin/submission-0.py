class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # top of minheap will have points closest to origin- keep popping and appending to result until we have k
        minheap=[]
        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            distance= math.sqrt(x**2 + y**2)
            minheap.append([distance,x,y])
        heapq.heapify(minheap) #this is faster than multiple heappush operations in for loop- directly converts list to heap
        res=[]
        while k>0:
            dist,x,y= heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res