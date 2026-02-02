class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(n)]

        def solve(i, isup, skipped):
            if i >= n -1:
                return 0
            if dp[i][isup][skipped] != -1:
                return dp[i][isup][skipped]
            res = 0

            # regular move
            # isup is true if next element should be greater and false if smaller

            if isup:
                if nums[i + 1] > nums[i]:
                    res = max(res, 1 + solve(i + 1, 0, skipped))
            else:
                if nums[i + 1] < nums[i]:
                    res = max(res, 1 + solve(i + 1, 1, skipped))
            
            # skip move -> trying to extend to i + 2
            if not skipped and i + 2 < n:
                if isup:
                    if nums[i + 2] > nums[i]:
                        res = max(res, 1 +solve(i + 2, 0, 1))
                else:
                    if nums[i + 2] < nums[i]:
                        res = max(res, 1 + solve(i + 2, 1, 1))

            dp[i][isup][skipped] = res
            return dp[i][isup][skipped]
        
        maxlen = 1
        for i in range(0, n):
            startup = 1 + solve(i, 1, 0) # assuming next is up
            startdown = 1 + solve(i , 0 , 0) # assuming next is down

            maxlen = max(maxlen, startup, startdown)
        
        return maxlen

        