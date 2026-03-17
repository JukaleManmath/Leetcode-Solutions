class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k= len(s1)
        if k > n:
            return False
        mp1 = defaultdict(int)
        mp2 = Counter(s1)

        l = 0
        for r in range(k):
            mp1[s2[r]] += 1
        
        if mp1 == mp2:
            return True

        for r in range(k , n):
            mp1[s2[r]] += 1
            mp1[s2[l]] -= 1
            if mp1[s2[l]] == 0:
                del mp1[s2[l]]
            l += 1

            if mp1 == mp2:
                return True
        return False
             