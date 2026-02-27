class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = 0
        for i in s:
            if  i == "0":
                zeros += 1
        if zeros == 0:
            return 0
        nodesets = [SortedList(range(0,n+1,2)), SortedList(range(1,n+1,2))]
        dist = [-1] *(n+1)
        q = deque()
        q.append(zeros)
        dist[zeros] = 0
        nodesets[zeros % 2].remove(zeros)

        while q:
            z = q.popleft()

            minF = max(0, k - n + z)
            maxF = min(k, z)
            max_newz = z + k - (2 * minF)
            min_newz = z + k - (2 * maxF)

            nodeset = nodesets[min_newz % 2]
            idx = nodeset.bisect_left(min_newz)

            while idx < len(nodeset) and nodeset[idx] <= max_newz:
                newz = nodeset[idx]
                if dist[newz] == -1:
                    dist[newz] = dist[z] + 1
                    if newz == 0:
                        return dist[newz]
                    q.append(newz)
                    nodeset.pop(idx)
        return -1