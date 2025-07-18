class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute force - sorting O(nlogn)
        # points.sort(key= lambda d: d[0]**2 + d[1]**2)
        # return points[:k]

        #-----minHeap O(klogn)------
        minHeap = []
        res = []
        for i in points:
            x , y = i[0], i[1]
            dis = abs(x**2 + y**2)
            minHeap.append([dis, x, y])
            
        heapq.heapify(minHeap)

        while k > 0:
            dis, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res