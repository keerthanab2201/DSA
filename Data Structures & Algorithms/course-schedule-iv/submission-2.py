class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # a,b means a is a prerequisite of b

        ''' #dfs solution- O((V+E)*m) where m is no of queries

        adj={i:[] for i in range(numCourses)}
        res=[]
        for pre,course in prerequisites:
            adj[course].append(pre)

        def dfs(course,prereq):
            if course==prereq:
                return True
            visiting.add(course)
            for pre in adj[course]:
                if pre not in visiting:
                    if dfs(pre,prereq): #IMP- Go explore the neighbor. If that recursive exploration finds the answer (True), then I also return True. If we just run dfs without IF statement, it will not break all the recursive function calls
                        return True
            return False

        for a,b in queries:
            visiting=set() # new set for each query/pair we are checking
            ans= dfs(b,a)
            res.append(ans)
        return res '''

        # kahns algo- O(V*(V+E)+m)
        adj= defaultdict(list) # maps prerequisite to courses
        indegree= [0]*numCourses # no of dependencies (prerequisites) for a course
        q= deque()
        prereq= defaultdict(set) # maintains a set of ALL (direct&indirect) prerequisites for each course 
        finish=0 #IMP- to track whether all courses can be processed
        for pre,course in prerequisites:
            adj[pre].append(course)
            indegree[course]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            course= q.popleft()
            for nei in adj[course]: #course and all its prerequisites are prerequisites of nei
                prereq[nei].add(course)
                prereq[nei].update(prereq[course]) #update() is a Python set method that adds all elements from another collection into a set
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        ans=[]
        for pre,crs in queries:
            ans.append(pre in prereq[crs])
        return ans
        

        


        
        