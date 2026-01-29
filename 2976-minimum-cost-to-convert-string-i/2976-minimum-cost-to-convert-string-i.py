class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target) or len(original) != len(changed):
            return -1

        n = len(source)
        g = defaultdict(list)
        for i in range(len(original)):
            g[original[i]].append([cost[i], changed[i]])
        
        needed_pairs = [(s, t) for s, t in zip(source, target) if s != t]
        if not needed_pairs:
            return 0
        
        starts = set( s for s, _ in needed_pairs)
        def shortestDist(graph, a):
            heap = [[0, a]]
            visited = set()
            dist = {a: 0}

            while heap:
                currdist , node = heapq.heappop(heap)
                if node in visited:
                    continue
                
                visited.add(node)
                for d , n in graph[node]:
                    newdist = currdist + d
                    if newdist < dist.get(n, float("inf")):
                        dist[n] = newdist
                        heapq.heappush(heap, (newdist, n))
                
            return dist
        
        best = {}
        for s in starts:
            best[s] = shortestDist(g, s)

        total = 0
        for i in range(n):
            if source[i] == target[i]:
                continue
            else:
                bd = best[source[i]].get(target[i], float("inf"))
                if bd == float("inf"):
                    return -1
                total += bd
        
        return total



        

        
