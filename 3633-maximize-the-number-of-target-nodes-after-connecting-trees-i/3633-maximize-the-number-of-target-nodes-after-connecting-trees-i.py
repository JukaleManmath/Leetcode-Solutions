class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1
        t1 , t2 = defaultdict(list), defaultdict(list)
        for u , v in edges1:
            t1[u].append(v)
            t1[v].append(u)
        for u , v in edges2:
            t2[u].append(v)
            t2[v].append(u)
        
        def dfs(node ,tree , dist, maxDist):
            if dist > maxDist:
                return 0
            cnt = 1
            for nei in tree[node]:
                if not visited[nei]:
                    visited[nei] = True
                    cnt += dfs(nei, tree, dist + 1, maxDist)
            return cnt
        
        countt2 = maxcount = 0
        for i in range(m):
            visited = [False for _ in range(m)]
            visited[i] = True

            countt2 = dfs(i, t2, 0 ,k-1)
            maxcount = max(maxcount, countt2)
        
        ans = [0 for _ in range(n)]
        for i in range(n):
            visited = [False for _ in range(n)]
            visited[i] = True
            cnt1 = dfs(i , t1, 0 , k)
            ans[i] = cnt1 + maxcount
        
        return ans
