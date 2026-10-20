class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # approach- use 2 minheaps
        available=[(x,i) for i,x in enumerate(servers)] # stores (server_weight, server_index) such that smallest available server is always at the top
        running=[] # stores finish_time of each task running on a server and its server_index
        heapq.heapify(available)
        time=0
        res=[]
        for i in range(len(tasks)):
            time= max(time,i) #imp
            if running and not available: #If no server is free, jump to the next finish time
                finish,idx= heapq.heappop(running)
                time= finish
                heapq.heappush(available,(servers[idx],idx))
            while running and time>=running[0][0]: # Release all servers that have finished
                finish,idx= heapq.heappop(running)
                heapq.heappush(available,(servers[idx],idx))
            # Assign the task to the best available server
            weight,idx= heapq.heappop(available)
            heapq.heappush(running,(time+tasks[i],idx))
            res.append(idx)
        return res

            


