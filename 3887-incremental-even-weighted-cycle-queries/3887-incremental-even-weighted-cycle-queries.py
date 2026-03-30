class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        p = [0] * n
        
        def find(x):
            if parent[x] != x:
                par= parent[x]
                parent[x] = find(parent[x])
                p[x]  ^= p[par]
            return parent[x]
        
        def union(u, v, w):
            ru = find(u)
            rv = find(v)

            if ru ==rv:
                return p[u] ^ p[v] == w
            
            parent[rv] = ru
            p[rv] = p[u] ^ p[v] ^ w

            return True
        
        res = 0
        for u , v, w in edges:
            if union(u , v, w):
                res += 1
        return res
 
        
            