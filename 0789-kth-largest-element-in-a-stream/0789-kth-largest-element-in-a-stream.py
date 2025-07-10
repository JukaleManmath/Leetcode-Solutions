class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.heap = []
        # self.k = k
        # for i in nums:
        #     heapq.heappush(self.heap, i)
        #     if len(self.heap) > self.k:
        #         heapq.heappop(self.heap)

        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # heapq.heappush(self.heap, val)
        # if len(self.heap) > self.k:
        #     heapq.heappop(self.heap)
        # return self.heap[0]
        
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)