# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        
        n = len(arr)
        i = 0
        while i+k <= len(arr):
            left = i
            right = i + k - 1
            while left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left+= 1
                right -= 1
            i += k
            
        for l in range(len(arr)-1):
            arr[l].next = arr[l+1]
        arr[n-1].next = None
        return arr[0]
