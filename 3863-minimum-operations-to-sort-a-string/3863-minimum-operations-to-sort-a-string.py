class Solution:
    def minOperations(self, s: str) -> int:
        sorts = "".join(sorted(s))
        if s == sorts:
            return 0
        n = len(s)
        if n == 2:
            return -1
        
        maxc = max(s)
        minc= min(s)

        if s[0] == maxc and s[n-1] == minc and s.count(maxc) == 1 and s.count(minc) == 1:
            return 3
        
        if s[0] == sorts[0] or s[n-1] == sorts[n-1]:
            return 1
        return 2
                
            
    