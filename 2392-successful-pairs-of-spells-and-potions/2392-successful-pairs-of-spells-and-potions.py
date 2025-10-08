class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n, m = len(spells) , len(potions)
        for i in range(n):
            l , r = 0 , m - 1
            spell = spells[i]
            found = m
            while l <= r:
                mid = l + (r - l) // 2
                if spell * potions[mid] >= success:
                    found = mid
                    r = mid - 1
                elif spell * potions[mid] < success:
                    l = mid + 1
            res.append(m - found)
        return res