class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        freq = [0] * value
        for i in range(n):
            rem = (nums[i] % value + value) % value
            freq[rem] += 1
        
        f = 0
        while freq[f % value]:
            freq[f % value] -= 1
            f = (f + 1) 
        return f