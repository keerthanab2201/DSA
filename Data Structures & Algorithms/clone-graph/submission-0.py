"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew={}
        if not node:
            return None
        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            clone= Node(node.val)
            oldtonew[node]= clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node) #Calling a function and returning a function's result are two different things.
