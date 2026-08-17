class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj= [[] for i in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        res=[]
        minh=float('inf')
        visited= set()
        def dfs(node,parent):
            height=0
            for nei in adj[node]:
                if nei==parent:
                    continue
                height= max(height,1+dfs(nei,node))
            return height
        for node in range(n):
            curh= dfs(node,-1)
            if curh==minh:
                res.append(node)
            elif curh<minh:
                res=[node]
                minh=curh
        return res