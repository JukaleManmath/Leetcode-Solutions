# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good = 0

        def dfs(node, prev):
            nonlocal good
            if not node:
                return 
            if node.val >= prev:
                good += 1
            dfs(node.left, max(node.val, prev))
            dfs(node.right, max(node.val, prev))
        
        dfs(root, float("-inf"))
        return good

            