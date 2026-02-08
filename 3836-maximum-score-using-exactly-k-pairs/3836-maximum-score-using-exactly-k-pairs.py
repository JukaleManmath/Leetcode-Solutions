class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n , m = len(nums1), len(nums2)
        # dp = {}
        # def rec(i , j , rem):
        #     if rem == 0:
        #         return 0

        #     if (i, j , rem) in dp:
        #         return dp[(i, j ,rem)]
                
        #     if i >= n or j >= m:
        #         return float("-inf")

        #     take = (nums1[i] * nums2[j] + rec(i+ 1, j + 1, rem - 1 ))
        #     notake = max(rec(i + 1, j , rem), rec(i, j + 1, rem))
        #     dp[(i, j ,rem)] =  max(take, notake)
        #     return dp[(i, j ,rem)]
        # return rec(0,0,k)

        dp = [[[float("-inf")] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                dp[i][j][0] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for x in range(1, k + 1):
                    dp[i][j][x] = max(dp[i][j][x], dp[i - 1][j][x], dp[i][j-1][x],dp[i-1][j-1][x-1] + nums1[i-1]*nums2[j-1])
        
        return dp[n][m][k]