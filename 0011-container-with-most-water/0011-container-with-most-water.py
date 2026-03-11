class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l , r = 0 , len(height) - 1
        while l < r:
            curr = (r - l ) * min(height[l], height[r])
            if curr > area:
                area = curr
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area