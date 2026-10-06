class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # approach- priority is to run the task (char) having highest occurance/frequency first
        # max heap- stores remaining count of tasks with most frequent on top
        # cooldown queue- stores (-count, cooldown/idletime)
        # After running a task, increase (-)count and append it to the queue with time when it will be available again (current time + n). 
        # When cooldown finishes, push it back onto the heap
        # If heap is empty but tasks are still in cooldown then jump current time forward (idle)
        counts= Counter(tasks) # counter maps each task to its frequency in the list
        maxheap= [-x for x in counts.values()]
        heapq.heapify(maxheap)
        time=0
        q=deque() 
        while maxheap or q:
            time+=1
            if not maxheap: #If no task is available, jump to the next available time
                time= q[0][1]
            else:
                count= heapq.heappop(maxheap)+1 # increment since -count (maxheap)
                if count!=0:
                    q.append([count,time+n])
            while q and q[0][1]<=time: #Move all tasks whose cooldown is finished
                heapq.heappush(maxheap, q.popleft()[0])
        return time
    
