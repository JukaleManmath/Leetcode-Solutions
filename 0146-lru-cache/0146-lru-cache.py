class Node:
    def __init__(self, key , val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.front = Node(0 , 0)
        self.end = Node(0, 0)

        self.front.nxt , self.end.prev = self.end , self.front

    def addtoend(self, node):
        last = self.end.prev
        last.next , self.end.prev = node, node
        node.prev, node.next = last, self.end

    def remove(self, node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next , nextnode.prev = nextnode, prevnode

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.addtoend(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.addtoend(self.cache[key])
        if len(self.cache) > self.cap:
            node = self.front.next
            self.remove(node)
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)