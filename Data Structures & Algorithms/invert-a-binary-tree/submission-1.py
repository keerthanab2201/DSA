# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # initialise stack with root
        # pop the current node from stack, swap its left and right nodes
        # push left and right nodes onto stack if present
        stack=[root]
        while stack:
            curr= stack.pop()
            curr.left, curr.right= curr.right, curr.left
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)    
        return root

        