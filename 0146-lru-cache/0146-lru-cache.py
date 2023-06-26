class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(None, None)
        self.right = Node(None, None)
        
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right 
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            # del self.cache[self.left.next.key]
            # self.remove(self.left.next)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




























# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.cap = capacity
#         self.left = Node(0, 0)
#         self.right = Node(0, 0)
        
#         self.left.next = self.right
#         self.right.prev = self.left
    
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev
        
#     def insert_right(self, node):
#         prev = self.right.prev
#         prev.next = self.right.prev = node
#         node.prev, node.next = prev, self.right
    
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert_right(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert_right(self.cache[key])
#         if len(self.cache) > self.cap:
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]