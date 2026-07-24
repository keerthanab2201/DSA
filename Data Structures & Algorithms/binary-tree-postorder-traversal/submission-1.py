# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # postorder traversal- left, right, current
        ''' recursive soln
        res=[]
        def postorder(node):
            if not node:
                return None
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        postorder(root)
        return res'''
        # iterative solution
        res=[]
        stack=[]
        curr=root
        lastvisited= None #imp
        while stack or curr:
            while curr:
                stack.append(curr)
                curr= curr.left
            # If right child exists and hasn't been processed
            if stack[-1].right and lastvisited!= stack[-1].right:
                curr=stack[-1].right
            else:
                lastvisited= stack.pop()
                res.append(lastvisited.val)
        return res
