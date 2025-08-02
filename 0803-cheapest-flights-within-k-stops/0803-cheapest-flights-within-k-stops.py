class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        inf = float("inf")
        dist = [[inf] * (k+5) for _ in range(n)]
        for u , v,  cst in flights:
            adj[u].append([v,cst])
        
        dist[src][0] = 0
        minheap = [(0,src, -1)]
        while len(minheap):
            cst , node, stops = heapq.heappop(minheap)
            if dst == node:
                return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue
            for nei , w in adj[node]:
                ncst = cst + w
                nextstops = stops + 1
                if dist[nei][nextstops + 1] > ncst:
                    dist[nei][nextstops + 1]= ncst
                    heapq.heappush(minheap, (ncst, nei, nextstops))
        return -1

        