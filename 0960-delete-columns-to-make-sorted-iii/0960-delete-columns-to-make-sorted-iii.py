class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        dp = [1] * m

        for i in range(m -2, -1, -1):
            for j in range(i + 1, m):
                for row in strs:
                    if row[i] > row[j]:
                        break
                else:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return m - max(dp)