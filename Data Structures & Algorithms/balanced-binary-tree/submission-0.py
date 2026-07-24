# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # returns height if balanced else returns -1 (height can never be negative)
            if not node:
                return True
            leftheight = dfs(node.left)
            rightheight = dfs(node.right)
            if leftheight==-1 or rightheight==-1:
                return -1
            if abs(leftheight-rightheight)>1:
                return -1
            return max(leftheight,rightheight)+1
        return dfs(root)!=-1
            
        
        