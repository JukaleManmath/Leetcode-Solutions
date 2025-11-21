class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        res = set()
        for i in s:
            right[i] -= 1

            for j in left:
                if right[j] > 0:
                    res.add((j , i))
            
            left.add(i)
        return len(res)