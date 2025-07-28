class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        def find(i):
            root = parent[i]
            if parent[root] != root:
                parent[i] = find(root)
                return parent[i]
            return root
        
        def union(i, j):
            pi = find(i)
            pj = find(j)

            if pi == pj:
                return False
            si = size[pi]
            sj = size[pj]
            if si < sj:
                parent[pi] = pj
                size[pj] += size[pi]
            else:
                parent[pj] = pi
                size[pi] += size[pj]
            return True
        
        for i, j in edges:
            if not union(i, j):
                return [i, j]
