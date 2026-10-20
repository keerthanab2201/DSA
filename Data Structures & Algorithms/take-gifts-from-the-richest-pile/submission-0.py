import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap= [-x for x in gifts]
        heapq.heapify(maxheap)
        res=0
        for i in range(k):
            maxpile= -heapq.heappop(maxheap)
            newpile= math.floor(math.sqrt(maxpile))
            heapq.heappush(maxheap,-newpile)
        while maxheap:
            res+= -heapq.heappop(maxheap)
        return res

