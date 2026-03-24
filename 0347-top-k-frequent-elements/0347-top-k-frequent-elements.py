class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minHeap = []

        for i , val in freq.items():
            heapq.heappush(minHeap, (val, i))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [ i for _, i in minHeap]
        
        

        # n = len(nums)
        # buckets= [[] for _ in range(n + 1)] 
        # freq = Counter(nums)
        # for i, val in freq.items():
        #     buckets[val].append(i)
        # print(buckets)
        # res = []
        # i = n
        # while k and i >= 0:
        #     if buckets[i]:
        #         for num in buckets[i]:
        #             res.append(num)
        #             k -= 1
        #     i -= 1

        # return res