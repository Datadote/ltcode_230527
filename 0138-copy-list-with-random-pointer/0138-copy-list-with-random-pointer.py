"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        do2n = {None: None}
        curr = head
        while curr:
            do2n[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            newNode = do2n[curr]
            newNode.next = do2n[curr.next]
            newNode.random = do2n[curr.random]
            curr = curr.next
        return do2n[head]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # old2new = {None: None}
        # cur = head
        # while cur:
        #     old2new[cur] = Node(cur.val)
        #     cur = cur.next
        # cur = head
        # while cur:
        #     copy = old2new[cur]
        #     copy.next = old2new[cur.next]
        #     copy.random = old2new[cur.random]
        #     cur = cur.next
        # return old2new[head]