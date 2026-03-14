class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n
        leftmax[0] = height[0]
        rightmax[n-1] = height[n-1]
        for i in range(1, n):
            leftmax[i] = max(height[i] , leftmax[i-1])
            rightmax[n-1-i] = max(height[n-1-i], rightmax[n-i])
        
        res = 0

        for i in range(n):
            res += min(leftmax[i], rightmax[i]) - height[i]
        return res
