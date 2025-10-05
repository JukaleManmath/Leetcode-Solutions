class MinStack:

    def __init__(self):
        self.stack = []
        self.minheap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minheap, val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        while self.minheap:
            minele = self.minheap[0]
            if minele in self.stack:
                return minele
            else:
                heapq.heappop(self.minheap)
            
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()