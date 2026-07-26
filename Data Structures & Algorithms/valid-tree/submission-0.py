class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''A graph is a valid tree if:
            It has no cycles
            It is fully connected
        '''
        # use dfs to detect a cycle
        if len(edges)!=n-1: # a valid tree with n nodes must have exactly (n-1) edges
            return False
        adj= [[] for node in range(n)] #adjacency list
        for node,nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        visited= set()

        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei==parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n

