class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m , n = len(text1), len(text2)
        dp = [[-1] * (n) for i in range(m)]
        def rec(i, j):
            if i == m or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            res = 0
            if text1[i] == text2[j]:
                res =  1 + rec(i + 1, j + 1)
            else:
                res = max(rec(i + 1, j), rec(i, j + 1))
            dp[i][j] = res
            return res
        return rec(0,0)