"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}

        # def dfs(node):
        #     if node in oldToNew:
        #         return oldToNew[node]
            
        #     cp = Node(node.val)
        #     oldToNew[node] = cp
        #     for i in node.neighbors:
        #         cp.neighbors.append(dfs(i))
        #     return cp
        # return dfs(node) if node else None

        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[curr].neighbors.append(oldToNew[nei])
        return oldToNew[node]


