# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder- left, current, right- dfs
        '''# recursive solution- trivial
        res=[]
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res'''
        # iterative solution- dfs
        res=[]
        stack=[]
        curr= root
        while curr or stack: #keep traversing depth and pushing onto stack until we reach end
            while curr:
                stack.append(curr)
                curr=curr.left
            curr= stack.pop()
            res.append(curr.val)
            curr= curr.right
        return res


        