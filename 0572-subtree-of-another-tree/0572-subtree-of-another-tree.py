# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # space comp - O(m + n) and time - O(m *n)
    def isIdentical(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)
        
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        