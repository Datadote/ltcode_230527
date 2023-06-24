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
        old2new = {None: None}
        cur = head
        while cur:
            old2new[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = old2new[cur]
            copy.next = old2new[cur.next]
            copy.random = old2new[cur.random]
            cur = cur.next
        return old2new[head]