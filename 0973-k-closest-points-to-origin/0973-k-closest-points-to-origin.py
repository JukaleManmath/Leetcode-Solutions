class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(minheap, (-dist, x, y))
            if len(minheap) > k:
                heapq.heappop(minheap)
        return [[x, y] for _, x, y in minheap]
        
        