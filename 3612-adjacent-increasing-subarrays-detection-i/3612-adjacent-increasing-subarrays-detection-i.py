class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isIncreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True
        n = len(nums)
        for i in range(n-k+1):
            j = i + k
            if j <= n-k and isIncreasing(nums[i:i +k]) and isIncreasing(nums[j:j +k]):
                return True
        return False