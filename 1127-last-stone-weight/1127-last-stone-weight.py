class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [ -s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y =  heapq.heappop(maxHeap)
            x =  heapq.heappop(maxHeap)
            if x > y:
                heapq.heappush(maxHeap, y - x)

        return abs(maxHeap[0]) if maxHeap else 0