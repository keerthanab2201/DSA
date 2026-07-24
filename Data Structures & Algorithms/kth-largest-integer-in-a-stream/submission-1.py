class KthLargest:
    #kth largest element is the smallest element among top k largest elements
    # use a min heap that maintains k elements- if it exceeds, pop/ remove smallest element
    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for i in nums:
            heapq.heappush(self.heap, i)
            if len(self.heap)>k:
                heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
                heapq.heappop(self.heap)
        return self.heap[0]
        
