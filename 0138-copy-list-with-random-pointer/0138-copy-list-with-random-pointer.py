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
        dummy = head

        while dummy:
            newNode = Node(dummy.val)
            newNode.next = dummy.next
            dummy.next = newNode
            dummy = dummy.next.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        dummy = head
        new = head.next
        while dummy:
            copy = dummy.next
            dummy.next = copy.next
            if copy.next:
                copy.next =copy.next.next
            dummy = dummy.next
        
        return new

        
        