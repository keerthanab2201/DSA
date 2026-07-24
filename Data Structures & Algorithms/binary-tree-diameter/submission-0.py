# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0 # diameter for a node will be height of left subtree + height of right subtree- we need to find the maximum
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            leftsubtree= dfs(node.left)
            rightsubtree= dfs(node.right)
            diameter= max(diameter, leftsubtree+rightsubtree)
            return 1+max(leftsubtree,rightsubtree)
        dfs(root)
        return diameter
            


