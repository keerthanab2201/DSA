class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we can use topological sort (using dfs)
        adj= {i:[] for i in range(numCourses)} # this maps each prereq to courses that can be taken after it
        for nxt, pre in prerequisites:
            adj[pre].append(nxt)
        visiting=set() #current recursion stack (detect cycles in a dfs path)
        visited=set() #already processed
        stack=[] #stores nodes after all neighbors are processed
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for nxt in adj[course]:
                if not dfs(nxt):
                    return False
            visiting.remove(course)
            visited.add(course)
            stack.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        stack.reverse()
        return stack
            

