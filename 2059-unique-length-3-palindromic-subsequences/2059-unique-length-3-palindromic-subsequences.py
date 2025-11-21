class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        res = set()
        for i in s:
            if right[i]:
                right[i] -= 1
                if right[i] == 0:
                    del right[i]
            for j in left:
                if j in right:
                    res.add((j , i))
            
            left.add(i)
        return len(res)