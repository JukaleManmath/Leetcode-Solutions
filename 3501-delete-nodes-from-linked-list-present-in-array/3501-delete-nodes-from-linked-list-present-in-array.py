# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not nums:
            return head
        nums = set(nums)
        dummy = ListNode(0,head)
        temp = dummy
        while temp.next:
            if temp.next.val in nums:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next