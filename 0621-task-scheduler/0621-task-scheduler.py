class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = Counter(tasks)
        minHeap = [-i for i in task_map.values()]
        heapq.heapify(minHeap)

        q = deque()
        time = 0
        while minHeap or q:
            time += 1
            if not minHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(minHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(minHeap, q.popleft()[0])
        return time