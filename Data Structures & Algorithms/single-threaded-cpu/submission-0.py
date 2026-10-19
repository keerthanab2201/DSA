class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''Use two stages:
        - Sorted tasks: Find tasks that have arrived.
        - Min heap: Choose the best task among those that have arrived.'''
        res=[]
        minheap=[] # minheap only stores and sorts those tasks which have arrived according to (processing_time, index)
        time=0
        i=0 # keeps track of current index in tasks array
        tasks= [(start,processing,idx)for idx,(start,processing) in enumerate(tasks)]
        tasks.sort() # sort tasks by enqueue/start time 

        while i<len(tasks) or minheap:
            if not minheap and time<tasks[i][0]: # if no task is available, jump to next available start time
                time= tasks[i][0]
            while i<len(tasks) and tasks[i][0]<=time: # add all tasks that have arrived to the minheap
                start,processing,idx= tasks[i]
                heapq.heappush(minheap,(processing,idx))
                i+=1
            processing,idx= heapq.heappop(minheap)
            res.append(idx)
            time+= processing

        return res



