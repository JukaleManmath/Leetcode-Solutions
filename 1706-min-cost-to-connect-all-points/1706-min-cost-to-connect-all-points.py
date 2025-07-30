# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n+1))
#         self.size = [1] * ( n + 1)
    
#     def find(self, i):
#         root = self.parent[i]
#         if self.parent[root] != root:
#             self.parent[i] = self.find(root)
#             return self.parent[i]
#         return root
#     def union(self, i , j):
#         pi = self.find(i)
#         pj = self.find(j)
#         if pi == pj:
#             return False
#         si = self.size[pi]
#         sj = self.size[pj]
#         if si < sj:
#             self.parent[pi] = pj
#             self.size[pj]  += self.size[pi]
#         else:
#             self.parent[pj] = pi
#             self.size[pi] += self.size[pj]
#         return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's algorithm using DSU
        # n = len(points)
        # dsu = DSU(n)
        # edges = []

        # for i in range(n):
        #     a1, b1 = points[i]
        #     for j in range(i +1 , n):
        #         a2 , b2 = points[j]
        #         dist = abs(a2 - a1) + abs(b2 -b1)
        #         edges.append((dist, i , j))
        # edges.sort()
        # res = 0
        # for dist, i , j in edges:
        #     if dsu.union(i, j):
        #         res += dist
        # return res

        # prims algo - using min heap (choose one min cost edge at a time which is not visited until the minheap is empty and all the vertices are traversed)
        n = len(points)
        adj = [[] for i in range(n)]

        for i in range(n):
            a1, b1 = points[i]
            for j in range(i+1,n):
                a2, b2 = points[j]
                dist = abs(a2 - a1) + abs(b2 - b1)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        visited = set()
        res = 0
        minheap = [(0,0)]
        while minheap:
            cost, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            res += cost
            for neicost , nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap,(neicost, nei))

        return res
