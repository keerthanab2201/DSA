# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # All values in the left subtree of a node are smaller than the node’s value.
    # All values in the right subtree are greater than the node’s value.
        if root==p or root==q:
            return root.val
        if (max(p.val,q.val))<root.val: # search left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val,q.val))>root.val: # search right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        