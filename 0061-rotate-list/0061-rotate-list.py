# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        n = 0
        curr = head
        dummy = ListNode(0, head)
        while curr:
            curr = curr.next
            n += 1
        
        k = k % n
        if  k == 0:
            return head
        ahead, behind = dummy, dummy
        for _ in range(k):
            ahead = ahead.next
        
        while ahead and ahead.next:
            ahead = ahead.next
            behind = behind.next
        
        temp = behind.next
        behind.next = ahead.next
        ahead.next = dummy.next
        dummy.next = temp

        return dummy.next
