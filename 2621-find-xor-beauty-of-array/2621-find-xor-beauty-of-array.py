class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        # total = []
        # for i in nums:
        #     for j in nums:
        #         for k in nums:
        #             total.append((i | j) & k)
        
        # res = [total[0]]
        # for i in range(1, len(total)):
        #     prev = res.pop()
        #     ans = prev ^ total[i]
        #     res.append( ans )
        
        # return res[0]

        # if we solve the equation consider all values same and 2 values same and all are different,
        # only the all values same gives us the result and all the other scenario gives 0
        # at the end we can just XOR all the values in the original nums which will give us optimised answer
        res = 0
        for i in nums:
            res = res ^ i
        return res
