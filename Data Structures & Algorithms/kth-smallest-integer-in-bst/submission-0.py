# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # perform inorder traversal
        count=0
        res=0
        def dfs(node):
            nonlocal count,res #declare as global variable otherwise each recursion call creates its own copy of count and sets it to 0 each time 
            if not node:
                return 0
            dfs(node.left)
            count+=1
            if count==k:
                res= node.val
            dfs(node.right)
        dfs(root)
        return res