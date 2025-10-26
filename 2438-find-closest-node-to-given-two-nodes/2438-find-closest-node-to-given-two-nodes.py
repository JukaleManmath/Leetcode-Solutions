class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2:
            return node1

        def dfs(node):
            dist = {}
            level = 0
            while node != -1 and node not in dist:
                dist[node] = level
                node = edges[node]
                level += 1
            return dist
        
        d1 , d2 = dfs(node1) , dfs(node2)
        res , minlen = -1, float("inf")

        for i in range(len(edges)):
            if i in d1 and i in d2:
                if max(d1[i] , d2[i]) < minlen:
                    minlen = max(d1[i], d2[i])
                    res = i
        return res
        

        
        