class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        n  =len(nums)

        def gcd(a, b):
            while b:
                a , b = b , a % b
            return a
        
        dp = {}

        def dfs(i, num, den):
            if i== n:
                return 1 if den == 1 and num == k else 0
            
            key = (i, num, den)
            if key in dp:
                return dp[key]
            
            total = 0
            new_num = num * nums[i]
            new_den = den
            g = gcd(new_num, new_den)
            total += dfs(i + 1, new_num // g, new_den // g)

            new_num = num
            new_den = den * nums[i]
            g = gcd(new_num, new_den)
            total += dfs(i + 1, new_num // g, new_den // g)

            total += dfs(i + 1, num, den)

            dp[key] = total
            return total
        return dfs(0, 1, 1)