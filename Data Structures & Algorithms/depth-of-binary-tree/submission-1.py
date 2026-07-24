# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''# recursive soln
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right)) '''
        
        #iterative soln- using dfs
        if not root:
            return 0
        stack= [[root,1]] #stack stores nodes + depth of traversal
        maxdepth=1
        while stack:
            curr, depth= stack.pop() #pop a node then append stack with its left and right subtrees
            maxdepth= max(depth,maxdepth)
            if curr.left:
                stack.append((curr.left,depth+1))
            if curr.right:
                stack.append((curr.right,depth+1))
        return maxdepth



