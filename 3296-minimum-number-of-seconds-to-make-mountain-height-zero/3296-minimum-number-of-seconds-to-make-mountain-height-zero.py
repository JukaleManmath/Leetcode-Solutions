class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = [(t, t, 1) for t in workerTimes]

        heapq.heapify(heap)

        while mountainHeight > 1:
            total , base , curr = heapq.heappop(heap)
            newcurr =  curr + 1
            total = (base * newcurr *(newcurr + 1))//2
            heapq.heappush(heap,(total, base, newcurr))
            mountainHeight -= 1
        return heapq.heappop(heap)[0]