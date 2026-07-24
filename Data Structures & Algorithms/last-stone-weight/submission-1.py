class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap- remember to take care of signs
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            x= abs(heapq.heappop(max_heap))
            y= abs(heapq.heappop(max_heap))
            if x!=y: #x is greater than y since it is popped first
                heapq.heappush(max_heap,-(x-y))
        if not max_heap:
            return 0
        else: 
            return -max_heap[0]