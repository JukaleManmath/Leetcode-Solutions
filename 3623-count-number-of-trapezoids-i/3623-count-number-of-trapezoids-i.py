class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = int(10 ** 9 + 7)

        mp = {}
        for pt in points:
            if pt[1] not in mp:
                mp[pt[1]] = 1
            else:
                mp[pt[1]] += 1
        for y, frq in mp.items():
            mp[y] = comb(frq, 2)
        ans = 0
        ps = 0
        for l in mp.values():
            ans = (ans + l * ps) % mod
            ps = (l + ps) % mod
        return ans