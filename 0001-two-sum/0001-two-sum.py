class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        n = len(nums)
        for i in range(n):
            num2 = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == num2:
                    return [i,j]
        return [0,0]

