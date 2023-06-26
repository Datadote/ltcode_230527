# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + carry
            carry = total // 10
            remainder = total % 10
            tail.next = ListNode(remainder)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            tail.next = ListNode(1)
            tail = tail.next
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy = tail = ListNode()
#         carry = 0
        
#         # carry_sum = total // 10
#         # remainder = total - carry_sum || reaminder = total % 10
        
#         while l1 and l2:
#             total = l1.val + l2.val + carry
#             if total < 10:
#                 tail.next = ListNode(total)
#                 carry = 0
#             else:
#                 tail.next = ListNode(total-10)
#                 carry = 1
#             l1 = l1.next
#             l2 = l2.next
#             tail = tail.next
#         while l1:
#             total = l1.val + carry
#             if total < 10:
#                 tail.next = ListNode(total)
#                 carry = 0
#             else:
#                 tail.next = ListNode(total-10)
#                 carry = 1
#             l1 = l1.next
#             tail = tail.next
#         while l2:
#             total = l2.val + carry
#             if total < 10:
#                 tail.next = ListNode(total)
#                 carry = 0
#             else:
#                 tail.next = ListNode(total-10)
#                 carry = 1
#             l2 = l2.next
#             tail = tail.next
#         if carry:
#             tail.next = ListNode(1)
#             tail = tail.next
#         return dummy.next