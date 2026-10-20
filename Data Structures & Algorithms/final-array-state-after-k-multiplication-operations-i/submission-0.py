class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minheap=[(x,i) for i,x in enumerate(nums)]
        heapq.heapify(minheap)
        for i in range(k):
            minval,idx= heapq.heappop(minheap)
            minval= minval*multiplier
            heapq.heappush(minheap,(minval,idx))
            nums[idx]= minval
        return nums

        