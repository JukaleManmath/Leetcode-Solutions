class Solution:
    # BFS in a DAG finding cycle - Kahn's Algo.
    def constructadj(self, n , prerequisites):
        adj = [[] for _ in range(n)]
        for ai, bi in prerequisites:
            adj[bi].append(ai)
        return adj
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.constructadj(numCourses, prerequisites)
        indegree = [0] * numCourses

        for bi in range(numCourses):
            for ai in adj[bi]:
                indegree[ai] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) != numCourses:
            return False
        return True