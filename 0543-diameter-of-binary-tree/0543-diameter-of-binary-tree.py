# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Brute force - O(n**2)
    # def maxHeight(self, root):
    #     if root is None:
    #         return 0
    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
        
    #     diameter = self.maxHeight(root.left) + self.maxHeight(root.right)

    #     sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    #     return max(diameter, sub)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return res

