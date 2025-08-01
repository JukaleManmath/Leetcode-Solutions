class MedianFinder:

    def __init__(self):
        self.small = [] # maxHeap
        self.large = [] #minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,(-1 * num))
        
        # every num in small is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, (-1 * val))
        
        #uneven size?
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, (-1 * val))
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, (-1 * val))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.small) < len(self.large):
            return self.large[0]
        
        return ((-1 * self.small[0]) + self.large[0]) / 2.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()