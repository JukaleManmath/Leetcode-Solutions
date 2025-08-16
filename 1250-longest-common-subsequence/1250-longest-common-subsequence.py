class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * (len(text2)) for _ in range(len(text1))]
        def dfs(s1, s2):
            if not s1 or not s2:
                return 0
            i , j = len(s1) - 1, len(s2) -1
            if memo[i][j] != -1:
                return memo[i][j]
            if s1[-1] == s2[-1]:
                memo[i][j] =  1 + dfs(s1[:-1], s2[:-1])
            else:
                memo[i][j] =  max(dfs(s1[:-1], s2), dfs(s1, s2[:-1]))
            return memo[i][j]

        return dfs(text1, text2)