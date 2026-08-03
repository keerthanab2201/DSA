# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxsofar):
            if not node:
                return 0
            if node.val>=maxsofar:
                res=1
                maxsofar= node.val
            else:
                res=0
            res+= dfs(node.left, maxsofar)
            res+= dfs(node.right, maxsofar)
            return res
        return dfs(root,root.val)