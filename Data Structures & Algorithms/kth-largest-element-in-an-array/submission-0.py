class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we use a max heap
        nums= [-x for x in nums]
        heapq.heapify(nums)
        # pop k elements to get the kth largest element
        while k>1:
            heapq.heappop(nums)
            k-=1
        return -heapq.heappop(nums)