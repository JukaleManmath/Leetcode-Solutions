class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target) or len(original) != len(changed):
            return -1

        n = len(source)
        g = defaultdict(list)
        for i in range(len(original)):
            g[original[i]].append([cost[i], changed[i]])
        
        def shortestDist(graph, a, b):
            heap = [[0, a]]
            visited = set()

            while heap:
                currdist , node = heapq.heappop(heap)

                if node == b:
                    return currdist
                if node in visited:
                    continue
                
                visited.add(node)
                for d , n in graph[node]:
                    newdist = currdist + d
                    heapq.heappush(heap, (newdist, n))
                
            return -1
        
        dist = {}
        total = 0
        for i in range(n):
            if source[i] == target[i]:
                continue
            else:
                if (source[i], target[i]) in dist:
                    total += dist[(source[i], target[i])]
                else:
                    curr = shortestDist(g, source[i], target[i])

                    if curr == -1:
                        return -1
                    
                    dist[(source[i], target[i])] = curr
                    total += curr
        
        return total



        

        
