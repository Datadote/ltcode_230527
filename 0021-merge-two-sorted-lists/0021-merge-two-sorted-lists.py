# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail, list1 = tail.next, list1.next
            else:
                tail.next = list2
                tail, list2 = tail.next, list2.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next