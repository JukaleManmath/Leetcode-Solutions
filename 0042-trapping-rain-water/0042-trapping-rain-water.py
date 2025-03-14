class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if not height:
            return 0
        res = 0
        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = height[0]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], height[i])
        
        rightmax[n-1] = height[n-1]
        for i in range(n-2, -1,-1):
            rightmax[i] = max(rightmax[i+1] , height[i])
        for i in range(n):
            res += min(leftmax[i] , rightmax[i]) - height[i]
        return res



     