class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        last_used = float("-inf")
        cnt = 0
        for i in nums:
            lower = i - k
            upper = i + k
            
            if last_used < lower:
                last_used = lower
                cnt += 1
            elif last_used < upper:
                last_used += 1
                cnt += 1
        return cnt