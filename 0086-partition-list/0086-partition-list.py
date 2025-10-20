# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        ahead = ListNode(0)
        res1 = ahead
        behind  = ListNode(0)
        res2 = behind
        while head:
            if head.val < x:
                res1.next = head
                res1 = res1.next
            else:
                res2.next = head
                res2 = res2.next
            head = head.next
        res2.next = None
        res1.next = behind.next
        return ahead.next