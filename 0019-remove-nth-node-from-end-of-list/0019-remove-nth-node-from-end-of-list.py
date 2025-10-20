# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # N = 0
        # curr = head
        # while curr:
        #     N += 1
        #     curr = curr.next
        
        # dummy = ListNode(0, head)
        # curr = head
        # prev = dummy
        # for i in range(N- n):
        #     prev = curr
        #     curr =curr.next
        
        # prev.next = curr.next
        # return dummy.next

        # two pointers approach
        dummy = ListNode(0, head)
        ahead , behind = dummy, dummy

        for _ in range(n + 1):
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            behind = behind.next
        
        behind.next = behind.next.next
        return dummy.next
