# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self, lists:List[Optional[ListNode]])-> ListNode:
        l1 = lists[0]
        l2 = lists[1]
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            l1 , l2 = lists.pop(0), lists.pop(0)
            l3 = self.mergeTwoList([l1,l2])
            lists.append(l3)
        return lists[0] if lists else None

