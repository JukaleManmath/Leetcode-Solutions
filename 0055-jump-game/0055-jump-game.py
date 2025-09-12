class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #we ccan keep track of the maximum index we can reach at current point and
        # if we can not move forward return False 
        # canjump = 0
        # n = len(nums)
        # for i in range(n-1):
        #     if canjump < i:
        #         return False
        #     canjump = max(canjump,i + nums[i])
        # return canjump >= n -1

        # we can also check in reverse that we can reach to the last index by coming back to 
        # first index and changing the target like wise

        n = len(nums)
        target = n -1
        for i in range(n-2,-1,-1):
            if i + nums[i] >= target:
                target = i
        return target == 0