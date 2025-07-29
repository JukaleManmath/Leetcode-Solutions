class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))

        # brute force - O(V*E)
        # dist = {node: float("inf") for node in range(1, n+1)}

        # def dfs(node, time):
        #     if time >= dist[node]:
        #         return
        #     dist[node] = time
        #     for nei , t in edges[node]:
        #         dfs(nei, t + time)
        # dfs(k,0)
        # res = max(dist.values())
        # return res if res < float("inf") else -1
            
        # Dijkstra's algoithm - Optimal O(ElogV) - uses minHeap for non-negative wts and selects the shortest next possible node having wt
        minheap = [(0, k)]
        t = 0
        visited = set()

        while minheap:
            t1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = t1
            for n2, t2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, (t1 + t2, n2))
        return t if len(visited) == n else -1