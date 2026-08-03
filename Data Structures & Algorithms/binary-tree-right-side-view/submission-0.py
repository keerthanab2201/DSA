# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # in each level- what is the rightmost node?
        res=[]

        def dfs(node,depth):
            if not node:
                return 
            if depth== len(res): # this is the first node at this depth -> append result
                res.append(node.val)
            dfs(node.right,depth+1) #visit right child first
            dfs(node.left,depth+1) #then visit left child
        
        dfs(root,0)
        return res

        