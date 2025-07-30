class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj = defaultdict(list)
        # tickets.sort()
        # for src, dst in tickets:
        #     adj[src].append(dst)
        
        # res = ["JFK"]
        # def dfs(src):
        #     if len(res) == len(tickets) + 1:
        #         return True
        #     if not adj[src]:
        #         return False
        #     tmp = list(adj[src])
        #     for i , v in enumerate(tmp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v):
        #             return True
        #         adj[src].insert(i, v)
        #         res.pop()
        #     return False
        # dfs("JFK")
        # return res

        adj = defaultdict(list)
        tickets.sort(reverse = True)
        for src, dst in tickets:
            adj[src].append(dst)
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        dfs("JFK")
        return res[::-1]