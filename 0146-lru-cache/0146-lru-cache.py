class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(None, None)
        self.right = Node(None, None)
        
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev, node.next = prev, self.right
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            tmp = self.cache[key]
            self.remove(tmp)
            self.insert(tmp)
            return tmp.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        tmp = Node(key, value)
        self.cache[key] = tmp
        self.insert(tmp)
        if len(self.cache) > self.cap:
            tmp = self.left.next
            self.remove(tmp)
            del self.cache[tmp.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)