class Solution:
    def residuePrefixes(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            if (i + 1) % 3 == len(Counter(s[:i+1])):
                ans += 1
        return ans