class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1), len(word2)
        # dp = [[-1] * (n + 1) for _ in range(m + 1)]

        # def rec(i , j):
        #     if i == m:
        #         return n - j
        #     if j == n:
        #         return m - i
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     if word1[i] ==word2[j]:
        #         return rec(i + 1, j + 1)
        #     dp[i][j] = 1 + min(rec(i + 1, j),  rec(i , j + 1), rec(i + 1, j + 1))
        #     return dp[i][j]
        # return rec(0, 0)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j
        
        for i in range(m -1,-1, -1):
            for j in range(n -1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        
        return dp[0][0]