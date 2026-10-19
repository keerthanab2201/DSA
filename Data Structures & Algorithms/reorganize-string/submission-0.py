class Solution:
    def reorganizeString(self, s: str) -> str:
        '''maxHeap efficiently gives us the most frequent character at any time. We pop the top character, add it to res, then push it back with decremented count after processing the next character. This delay ensures we never place the same character twice in a row. If the heap is empty but we still have a prev pending character, reorganization failed.'''
        # similar approach to task scheduler
        res= []
        maxheap=[] # stores (-count,character) with most frequent at the top
        prev= None # tracks previously used element and its updated count- cannot be immediately reused
        # IMP- temporarily remove the character you just used from the heap, so it cannot be selected again on the very next iteration. You only put it back after selecting a different character.
        
        count= Counter(s)
        maxheap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxheap)

        while prev or maxheap:
            if prev and not maxheap:
                return ""
            count,char= heapq.heappop(maxheap)
            res.append(char)
            count+=1
            if prev:
                heapq.heappush(maxheap,prev)
                prev= None
            if count!=0:
                prev= (count,char)
        return "".join(res)



