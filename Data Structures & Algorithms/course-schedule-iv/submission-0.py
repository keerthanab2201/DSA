class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # a,b means a is a prerequisite of b
        adj={i:[] for i in range(numCourses)}
        res=[]
        for i,j in prerequisites:
            adj[j].append(i)
        #visited= set()

        def dfs(node,pre):
            if node==pre:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei,pre): #IMP- Go explore the neighbor. If that recursive exploration finds the answer (True), then I also return True. If we just run dfs without IF statement, it will not break all the recursive function calls
                        return True
            return False
        for a,b in queries:
            visited=set()
            ans= dfs(b,a)
            res.append(ans)
        return res


        
        