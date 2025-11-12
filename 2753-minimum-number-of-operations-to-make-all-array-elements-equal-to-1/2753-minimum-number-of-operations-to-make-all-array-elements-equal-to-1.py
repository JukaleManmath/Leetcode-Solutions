class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt1 , o_gcd = 0, 0
        n = len(nums)
        for i in nums:
            if i == 1:
                cnt1 += 1
            o_gcd = math.gcd(o_gcd, i)
        
        if cnt1 > 0:
            return n - cnt1
        
        if o_gcd > 1:
            return -1
        
        min_len = n
        for i in range(n):
            cur = nums[i]
            if cur == 1:
                min_len = 1
                break
            
            for j in range(i+1, n):
                cur = math.gcd(cur, nums[j])
                if cur == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return min_len + n - 2
        

    
            
        

                