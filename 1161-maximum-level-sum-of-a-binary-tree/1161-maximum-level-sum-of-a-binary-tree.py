# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        maxval = float("-inf")
        level = 0
        curr = 0
        while q:
            curr += 1
            newsum = 0
            for i in range(len(q)):
                node = q.popleft()
                newsum += node.val 
                if node.left:
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            if newsum > maxval:
                maxval = newsum
                level = curr
        return level