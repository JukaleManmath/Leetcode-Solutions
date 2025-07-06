# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #  Brute force - O(n**2)
    # def maxHeight(self, root):
    #     if root is None:
    #         return 0
    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return True
    #     left = self.maxHeight(root.left)
    #     right = self.maxHeight(root.right)
    #     if (left > right and left - right > 1 ) or (right > left and right - left > 1):
    #         return False
        
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True

        def dfs(root):
            nonlocal flag
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                flag = False
            return 1 + max(left, right)
        
        dfs(root)
        return flag
