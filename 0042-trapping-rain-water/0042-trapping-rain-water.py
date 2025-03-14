class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        l , r = 0 , len(height) - 1
        leftmax , rightmax = height[l] , height[r]

        res = 0
        while l < r:
            if leftmax <= rightmax:
                res += leftmax - height[l] if leftmax - height[l] > 0 else 0
                l += 1
                leftmax = max(leftmax , height[l])
            else:
                res += rightmax - height[r] if rightmax - height[r] > 0 else 0
                r -= 1
                rightmax = max(rightmax , height[r])
        return res