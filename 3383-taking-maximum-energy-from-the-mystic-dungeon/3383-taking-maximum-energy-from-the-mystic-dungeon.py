class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = float("-inf")
        n = len(energy)
        # for i in range(n):
        #     curr = energy[i]
        #     for j in range(i + k , n , k):
        #         curr += energy[j]
        #     res = max(res, curr)
        
        # return res

        dp = [0] * n
        for i in range(n-1, -1, -1):
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)
            res = max(res, dp[i])
        
        return res