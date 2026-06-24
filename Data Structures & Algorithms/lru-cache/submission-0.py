class Node:

    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache:
            #node is already present, update value
            self.remove(self.cache[key])
            self.insert(node)
        else:
            if self.size<self.capacity:
                #insert at head
                self.insert(node)
            else:
                #delete lru from tail and cache and insert at head
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
                self.insert(node)

        self.cache[key] = node
    
    def insert(self, node: Node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        self.size += 1

    def remove(self, node: Node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
        self.size -= 1