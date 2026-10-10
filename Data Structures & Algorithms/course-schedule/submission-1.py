class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # directed graph i.e course->prerequisite
        '''
        # dfs soln (cycle detection)-all courses must process without cycle
        premap= {i:[] for i in range(numCourses)} #hashmap- course to list of prerequisites
        for course, prereq in prerequisites:
            premap[course].append(prereq)

        visiting= set() # stores all visited courses along current dfs path

        def dfs(course):
            if course in visiting: # cycle is detected
                return False
            if premap[course]==[]: # base case- at the end of a path, last node points to nothing
                return True
            visiting.add(course)
            for prereq in premap[course]: #expore all its prerequisites (neighbours)
                if not dfs(prereq):
                    return False
            visiting.remove(course) #every node must be removed when its DFS finishes
            premap[course]=[] #we have already proved this path is safe(no cycle)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True'''

        # topological sort (kahns algo)
        adj= defaultdict(list) # maps prerequisite->courses
        indegree= [0]*numCourses # no of dependencies (arrows pointing inwards) for each course
        for course,pre in prerequisites:
            adj[pre].append(course)
            indegree[course]+=1
        q= deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i) #at any time queue will contain those nodes having no dependencies- can safely be added to result (topological sort)
        finish=0
        while q:
            course= q.popleft() # pop node from queue and add to result
            finish+=1
            for nei in adj[course]:
                indegree[nei]-=1 # we need to remove course from graph
                if indegree[nei]==0:
                    q.append(nei)
        return finish==numCourses
            
        
        

            
            
        

