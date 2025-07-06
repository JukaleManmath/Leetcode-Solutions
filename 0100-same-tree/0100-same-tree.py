# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root, res):
            if root is None:
                res.append(None)
                return 
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
        res1 = []
        res2 = []
        dfs(p, res1)
        dfs(q, res2)
        
        return res1 == res2
        
        

