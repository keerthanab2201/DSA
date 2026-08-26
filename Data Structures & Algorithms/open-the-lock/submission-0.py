class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # starting from "0000", we want to find the shortest path to the target while avoiding deadends (bfs) 
        # each node in graph is a lock combination
        if target=="0000":
            return 0
        if "0000" in deadends:
            return -1
        steps=0
        visited= set(deadends) # set of states we are not allowed to visit/ have already visited
        q= deque(["0000"])
        visited.add("0000")

        # each level i will have all nodes that are i steps away from 0000

        while q:
            steps+=1 #we're about to explore all states that are 1 move away
            for _ in range(len(q)):
                lock= q.popleft() #now generate all possible locks reachable by 1 move from this node
                for i in range(4): #there are 4 wheels- explore each individually
                    for j in [-1,1]: #for each wheel- we can either move backwards or forwards
                        #thus each lock has 4 wheels x 2 directions= 8 neighbours
                        newdigit= str((int(lock[i]) + j + 10) % 10) #handles wraparound
                        nextlock= lock[:i] + newdigit + lock[i+1:]
                        if nextlock in visited:
                            continue
                        if nextlock==target:
                            return steps
                        q.append(nextlock)
                        visited.add(nextlock)
        return -1


        
