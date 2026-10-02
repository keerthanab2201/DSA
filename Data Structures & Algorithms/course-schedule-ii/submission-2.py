class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        return stack
            

