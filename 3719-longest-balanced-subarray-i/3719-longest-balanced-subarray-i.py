class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n  = len(nums)
        if n == 1:
            return 1
        res = 0
        for i in range(n):
            s = set()
            even , odd = 0, 0
            for j in range(i, n):
                if nums[j] not in s:
                    if nums[j] % 2 != 0:
                        even += 1
                    else:
                        odd += 1
                s.add(nums[j])
                if even == odd:
                    if j - i + 1 > res:
                        res  = j - i + 1
        return res
        

                 
            

