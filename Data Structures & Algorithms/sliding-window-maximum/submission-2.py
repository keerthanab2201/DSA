class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a max heap- stores negative of the numbers so that max is always at the top (heap[0])
        # here we are storing tuples in the heap (value,index)
        heap=[]
        res=[]
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i],i)) #heap automatically maintains max element at the top
            if i>=k-1: 
                while heap[0][1]<=i-k: #index of top should be inside the sliding window
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res

        
        
        
        ''' #brute force- o(nk) time
        l=0
        res=[float('-inf')]*(len(nums)-k+1)
        for l in range(len(nums)-k+1):
            r=l
            while r<l+k:
                res[l]=max(res[l],nums[r])
                r+=1
        return res'''
        