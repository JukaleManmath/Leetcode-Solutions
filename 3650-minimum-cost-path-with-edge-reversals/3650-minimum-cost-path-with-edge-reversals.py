class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, 2*w])
        
        visited = [False] * n
        dist = [float("inf")] * n
        dist[0] = 0
        pq = [[0,0]]

        while pq:
            currdist, currnode = heapq.heappop(pq)

            if currnode == n-1:
                return currdist
            
            if visited[currnode]:
                continue
            visited[currnode] = True

            for v, w in graph[currnode]:
                newdist = currdist + w
                if newdist < dist[v]:
                    dist[v] = newdist
                    heapq.heappush(pq, [newdist, v])
        return -1