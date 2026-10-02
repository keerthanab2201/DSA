class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # a,b means a is a prerequisite of b
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
        return res


        
        