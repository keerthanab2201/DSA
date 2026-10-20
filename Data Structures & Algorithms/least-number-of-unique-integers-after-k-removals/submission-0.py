class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # we prioritise removing least frequent elements first
        count= Counter(arr)
        minheap=[]
        for x in count:
            minheap.append((count[x],x))
        heapq.heapify(minheap)
        for i in range(k):
            freq,element= heapq.heappop(minheap)
            if freq-1>0:
                heapq.heappush(minheap, (freq-1,element))
        return len(minheap)
            

