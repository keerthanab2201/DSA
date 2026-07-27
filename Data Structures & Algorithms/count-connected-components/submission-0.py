class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # start dfs from a new unvisited node- visit all nodes in its connected component
        # Every time we start DFS from a new unvisited node, we’ve found one new component
        adj=[[] for node in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited= set()
        components=0
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components+=1
        return components
                