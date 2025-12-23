class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        maxval = 0
        ans = 0
        for s, e , v in events:
            while pq and pq[0][0] < s:
                maxval = max(maxval, heapq.heappop(pq)[1])
            ans = max(ans, maxval + v)
            heapq.heappush(pq, (e,v))
        return ans