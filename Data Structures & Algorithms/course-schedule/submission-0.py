class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # directed graph i.e course->prerequisite
        # use dfs
        # all courses must process without cycle

        # first map each course to its prerequisites
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
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course) #every node must be removed when its DFS finishes
            premap[course]=[] #we have already proved this path is safe(no cycle)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            
            
        

