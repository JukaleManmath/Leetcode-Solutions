# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [root.val]
        def dfs(root):
            nonlocal max_sum
            if root is None:
                return 0
            left = dfs(root.left) 
            right = dfs(root.right)
            left = max(0,left)
            right = max(0,right)

            curr_sum = root.val + left + right
            max_sum[0] = max(max_sum[0], curr_sum)
            return root.val + max(left, right)
        path_sum = dfs(root)
        return max_sum[0]
