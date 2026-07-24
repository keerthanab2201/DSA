# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse the given root (dfs) and at each node check if subtree is same as subroot (same binary tree logic)
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: optional[TreeNode], q: optional[TreeNode])->bool:
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        return False
        