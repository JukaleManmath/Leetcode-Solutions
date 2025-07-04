class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        # Brute Force
        # self.cache = []
        # self.capacity = capacity

        self.capacity = capacity
        self.cache = {} # HashMap for storing the nodes of Doubly linkedlist and getting operations in O(1) complexty

        self.left , self.right = Node(0, 0), Node(0,0)
        self.left.next , self.right.prev = self.right, self.left

    def remove(self, node):
        prev , nxt = node.prev, node.next
        prev.next, nxt.prev= nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        # BF
        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         tmp = self.cache.pop(i)
        #         self.cache.append(tmp)
        #         return tmp[1]
        # return -1

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #BF
        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         tmp = self.cache.pop(i)
        #         tmp[1] = value
        #         self.cache.append(tmp)
        #         return 

        # if self.capacity == len(self.cache):
        #     self.cache.pop(0)
        
        # self.cache.append([key, value])

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)