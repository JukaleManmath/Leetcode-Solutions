class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memoization
        # memo = [[-1] * (len(text2)) for _ in range(len(text1))]
        # def dfs(s1, s2):
        #     if not s1 or not s2:
        #         return 0
        #     i , j = len(s1) - 1, len(s2) -1
        #     if memo[i][j] != -1:
        #         return memo[i][j]
        #     if s1[-1] == s2[-1]:
        #         memo[i][j] =  1 + dfs(s1[:-1], s2[:-1])
        #     else:
        #         memo[i][j] =  max(dfs(s1[:-1], s2), dfs(s1, s2[:-1]))
        #     return memo[i][j]

        # return dfs(text1, text2)

        # Bottom -up
        dp = [[0 for _ in range(len(text2) + 1)]
                    for _ in range(len(text1) + 1)]
        m , n = len(text1), len(text2) 
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j + 1])
        return dp[0][0]
