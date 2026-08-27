class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a frequency map for each element and use (frequency,number) to sort the minheap
        # minheap stores smallest frequency at top
        # when size of minheap>k, pop 
        count= defaultdict(int)
        heap=[]
        for i in nums:
            count[i]+=1
        for num in count.keys():
            heapq.heappush(heap, (count[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            freq,num= heapq.heappop(heap)
            res.append(num)
        return res


        
        