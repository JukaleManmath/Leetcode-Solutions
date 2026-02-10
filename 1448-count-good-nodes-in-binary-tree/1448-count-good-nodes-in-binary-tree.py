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

        def dfs(node, prev):
            if not node:
                return 0
            good = 0
            if node.val >= prev:
                good += 1
            good += dfs(node.left, max(node.val, prev))
            good += dfs(node.right, max(node.val, prev))
            return good
        
        return dfs(root, float("-inf"))

            