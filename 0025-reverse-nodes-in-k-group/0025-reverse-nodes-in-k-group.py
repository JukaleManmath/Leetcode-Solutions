# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        loop = n // k

        curr = head
        prev = dummy
     
        for _ in range(loop):
            tail = curr
            prev_node = None

            for _ in range(k):
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp
            
            tail.next = curr
            prev.next = prev_node
            prev = tail
        return  dummy.next



        

            