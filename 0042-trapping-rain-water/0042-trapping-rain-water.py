class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # left = [0] * n
        # right = [0] * n

        # left[0] = height[0]
        # for i in range(1, n):
        #     left[i] = max(left[i-1],height[i] )
        
        # right[n-1] = height[n-1]
        # for i in range(n-2, -1, -1):
        #     right[i] = max(right[i+1],height[i] )
        
        # res = 0
        # for i in range(n):
        #     res += min(left[i],right[i]) - height[i]
        # return res

        l , r = 0 , n -1
        left, right = height[l] , height[r]
        res = 0
        while l < r:
            if left <= right:
                l += 1
                left = max(left, height[l])
                res += left - height[l]
            else:
                r -= 1
                right = max(right, height[r])
                res += right - height[r]
        
        return res