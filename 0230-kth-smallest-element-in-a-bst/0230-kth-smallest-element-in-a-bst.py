# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        def dfs(root, res):
            if not root:
                return res
            res.append(root.val)

            if root.left:
                res = dfs(root.left, res)
            if root.right:
                res = dfs(root.right, res)
            
            return res
        res = dfs(root, [])
        res.sort()
        return res[k-1]