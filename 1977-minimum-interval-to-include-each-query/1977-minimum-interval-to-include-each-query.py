class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # new = [[i[0], i[1], i[1]-i[0] + 1] for i in intervals]
        # new.sort(key=lambda x:(x[2],x[0],x[1]))
        # q = 0
        # res =[]
        
        # while q < len(queries):
        #     flag = True
        #     for i in new:
        #         if i[0] <= queries[q] <= i[1]:
        #             res.append(i[2])
        #             q += 1
        #             flag = False
        #             break
        #     if flag:
        #         q += 1
        #         res.append(-1)
               
        # return res

        intervals.sort()
        minHeap = []
        res , i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r= intervals[i]
                heapq.heappush(minHeap,(r-l+1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
