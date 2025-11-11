class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        res = 0
        l = len(strs)
        mp = defaultdict(list)
        for s in strs:
            mp[s] = Counter(s)

        dp = {}
        def dfs(i, cur_m, cur_n):
            if i >= l:
                return 0
            if (i, cur_m, cur_n) in dp:
                return dp[(i, cur_m, cur_n)]
            dp[(i, cur_m, cur_n)] = dfs(i + 1, cur_m, cur_n)
            if cur_m >= mp[strs[i]]["0"] and  cur_n >= mp[strs[i]]["1"]:
                dp[(i, cur_m, cur_n)] = max(dp[(i, cur_m, cur_n)], 1 + dfs(i + 1 , cur_m - mp[strs[i]]["0"], cur_n - mp[strs[i]]["1"]))
            
            return dp[(i, cur_m, cur_n)]
        
        return dfs(0,m,n)