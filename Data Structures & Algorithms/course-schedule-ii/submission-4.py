class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        '''#dfs soln
        adj= {i:[] for i in range(numCourses)} # adjacency list maps each course to its prerequisites
        for course,pre in prerequisites:
            adj[course].append(pre)
        visiting=set() #current recursion stack/dfs path (to detect cycles in the path)
        visited=set() #courses which have already processed and validated (avoids doing repeated work). In course schedule I, we just removed the processed courses from adj list but here we want an ordering in answer so we use this additional set
        stack=[] #stores nodes in order after all neighbors are processed (final answer)
        def dfs(course):
            if course in visiting: 
                return False
            if course in visited:
                return True
            visiting.add(course) # add course to current dfs path
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course) # remove course to current dfs path
            visited.add(course) # this course has been processed and is safe/valid
            stack.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return stack'''

        #topological sort soln (kahn's algo)
        adj= defaultdict(list) # maps prerequisite to courses
        indegree= [0]*numCourses # no of dependencies (prerequisites) for a course
        q= deque()
        res=[]
        finish=0 #IMP- to track whether all courses can be processed
        for course,pre in prerequisites:
            adj[pre].append(course)
            indegree[course]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            course= q.popleft()
            res.append(course)
            finish+=1
            for nei in adj[course]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return res if finish==numCourses else []
        
            

