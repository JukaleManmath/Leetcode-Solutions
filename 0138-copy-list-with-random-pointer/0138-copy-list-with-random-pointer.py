"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        hash = {}
        curr = head
        new_head = Node(curr.val)
        hash[curr] = new_head
        while curr.next:
            curr = curr.next
            new_head.next = Node(curr.val)
            new_head = new_head.next
            hash[curr] = new_head
        
        curr = head
        while curr:
            temp = hash[curr]
            temp.random = hash.get(curr.random)
            curr = curr.next
        return hash[head]