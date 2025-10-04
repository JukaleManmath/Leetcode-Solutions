class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        l , r = 0 , len(height) - 1
        while l < r:
            container = min(height[l], height[r]) * (r - l)
            water = max(water, container)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return water