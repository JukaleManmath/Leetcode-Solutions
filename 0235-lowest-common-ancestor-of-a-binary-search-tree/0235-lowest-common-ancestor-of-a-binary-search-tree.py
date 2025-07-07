# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Recursive dfs approach - O(h) time and space O(h) - h height of the tree
        # if not root or not p or not p:
        #     return None
        # max_val = max(p.val, q.val)
        # min_val = min(p.val, q.val)

        # if root.val <= max_val and root.val >= min_val:
        #     return root
        # if root.val < min_val:
        #     return self.lowestCommonAncestor(root.right, p , q)
        # return self.lowestCommonAncestor(root.left, p , q)

        # Iterative approach - time complexity O(h) , space complexity o(1)
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr 