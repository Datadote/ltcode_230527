# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            if total < 10:
                tail.next = ListNode(total)
                carry = 0
            else:
                tail.next = ListNode(total-10)
                carry = 1
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        while l1:
            total = l1.val + carry
            if total < 10:
                tail.next = ListNode(total)
                carry = 0
            else:
                tail.next = ListNode(total-10)
                carry = 1
            l1 = l1.next
            tail = tail.next
        while l2:
            total = l2.val + carry
            if total < 10:
                tail.next = ListNode(total)
                carry = 0
            else:
                tail.next = ListNode(total-10)
                carry = 1
            l2 = l2.next
            tail = tail.next
        if carry:
            tail.next = ListNode(1)
            tail = tail.next
        return dummy.next