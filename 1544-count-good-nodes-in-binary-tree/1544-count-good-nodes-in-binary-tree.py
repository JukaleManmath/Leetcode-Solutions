# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_till = root.val
        good = 0
        q = deque()
        q.append((root, max_till))
        while q:
            node, max_till = q.popleft()
            if node:
                if node.val >= max_till:
                    good += 1
                if node.val > max_till:
                    max_till = node.val
                
                if node.left:
                    q.append((node.left, max_till))
                if node.right:
                    q.append((node.right, max_till))
        return good

                



        