class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        l = [0] * n
        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                l[i] = l[i-1]
            else:
                l[i] = i
        
        r = [n-1] * n
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i + 1]:
                r[i] = r[i + 1]
            else:
                r[i] = i
        
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            start = l[i]
            le = i - start + 1
            dp[i] = (le *(le +1))// 2
            if start:
                dp[i] += dp[start - 1]
    
        res = []
        for start , end in queries:
            ans = dp[end] - (dp[start - 1] if start else 0)
            ans -= (start - l[start]) * (min(r[start], end) - start + 1)
            res.append(ans)
        return res
        
        