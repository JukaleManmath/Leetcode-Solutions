class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        Sum = sum(nums)
        if Sum % 2 != 0:
            return False
        target = Sum // 2

        prev = [False for _ in range(target + 1)]
    
        prev[0] = True
        if nums[0] <= target:
            prev[nums[0]] = True

        for i in range(1, n):
            curr = [False for _ in range(target + 1)]
            for j in range(1, target+1):          
                notake = prev[j]
                take = False
                if nums[i] <= j:
                    take = prev[j - nums[i]]
                curr[j] = take or notake
            prev = curr
        return prev[target]
                 