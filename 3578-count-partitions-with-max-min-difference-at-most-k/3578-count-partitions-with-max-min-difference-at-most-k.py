class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        dp = [0] * n
        ps = [0] * (n  +1)

        mx = deque()
        mn = deque()

        left = 0

        for right in range(n):
            while mx and mx[-1] < nums[right]:
                mx.pop()
            mx.append(nums[right])

            while mn and mn[-1] > nums[right]:
                mn.pop()
            mn.append(nums[right])

            while mx[0] - mn[0] > k:
                if mx[0] == nums[left]:
                    mx.popleft()
                if mn[0] == nums[left]:
                    mn.popleft()
                left += 1
            if left == 0:
                dp[right] = (ps[right] + 1) % mod
            else:
                dp[right] = (ps[right] - ps[left - 1]) % mod
            ps[right + 1] = (ps[right] + dp[right]) % mod 
        return dp[-1] % mod
 