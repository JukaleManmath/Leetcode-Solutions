class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minHeap = []

        for i , val in freq.items():
            heapq.heappush(minHeap, (-val, i))
        
        res = []
        while k:
            _, num = heapq.heappop(minHeap)
            res.append(num)
            k -= 1
        return res