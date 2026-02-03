class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        def increasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[ i -1]:
                    return False
            return True
        
        def decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] >= arr[i -1]:
                    return False
            return True
        
        for i in range(1, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if increasing(nums[:i + 1]) and decreasing(nums[i:j + 1]) and increasing(nums[j:]):
                    return True
        
        return False