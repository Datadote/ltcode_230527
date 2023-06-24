# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev, second = second, tmp
        first = head
        second = prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         second = slow.next
#         slow.next = None
        
#         prev = None # second == cur
#         while second:
#             nxt = second.next
#             second.next = prev
#             prev = second
#             second = nxt
        
#         list1, list2 = head, prev
#         while list2:
#             tmp1, tmp2 = list1.next, list2.next
#             list1.next = list2
#             list2.next = tmp1
#             list1 = tmp1
#             list2 = tmp2
        
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         second = slow.next
#         slow.next = None
        
#         # Reverse 2nd half, prev + second
#         prev = None
#         while second:
#             nxt = second.next
#             second.next = prev
#             prev = second
#             second = nxt
#         second = prev
        
#         # merge
#         while second:
#             nxt1, nxt2 = head.next, second.next
#             head.next = second
#             second.next = nxt1
#             head = nxt1
#             second = nxt2