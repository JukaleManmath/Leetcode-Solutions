class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u ,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        online = set()
        station_group = {}
        minheaps = defaultdict(list)

        def dfs(station, group_id):
            if station in online:
                return
            online.add(station)
            station_group[station] = group_id
            heappush(minheaps[group_id], station)

            for nei in adj[station]:
                dfs(nei, group_id)

        for i in range(1 , c+1):
            dfs(i, i)
        
        res = []
        for q_type, q_station in queries:
            if q_type == 1:
                if q_station in online:
                    res.append(q_station)
                    continue
                gid = station_group[q_station]
                minheap = minheaps[gid]
                while minheap and minheap[0] not in online:
                    heappop(minheap)
                if minheap:
                    res.append(minheap[0])
                else:
                    res.append(-1)
            else:
                online.discard(q_station)
        return res