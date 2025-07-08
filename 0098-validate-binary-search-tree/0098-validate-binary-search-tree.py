# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS - the logic here is when from an root we move to the right in a BST all the values in the right
        # should be greater the root and in the left should less than root
        # so we set max_value while moving in left as root.val and min_val moving right as root.val
        # recursively performing this logic gets the correct answer using DFS.
        def dfs(root, left, right):
            if not root:
                return True
            
            if not( left < root.val < right):
                return False
            
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        return dfs(root, float("-inf"), float("inf"))
            


        