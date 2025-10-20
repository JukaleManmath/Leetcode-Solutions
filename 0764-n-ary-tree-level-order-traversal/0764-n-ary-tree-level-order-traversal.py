"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        res = []
        q = deque([root])
        while q:
            level = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level.append(curr.val)
                for child in curr.children:
                    q.append(child)
            res.append(level)
        return res