class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algo just storing the order
        adj = [[] for _ in range(numCourses)]
        for ai, bi in prerequisites:
            adj[bi].append(ai)
        
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
        return res if len(res) == numCourses else []