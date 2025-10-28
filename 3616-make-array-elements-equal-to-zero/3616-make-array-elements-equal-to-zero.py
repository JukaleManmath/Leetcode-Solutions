class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # def simulate(i ,d):
        #     arr = nums[:]
        #     while 0 <= i < len(arr):
        #         if arr[i] == 0:
        #             i += d
        #         else:
        #             arr[i] -= 1
        #             d *= -1
        #             i += d
        #     return all(x == 0 for x in arr)
        
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         if simulate(i, 1): res+= 1
        #         if simulate(i, -1): res += 1
        # return res

        total = sum(nums)
        ps = [nums[0]]
        for i in range(1, len(nums)):
            ps.append(nums[i] + ps[-1])
        
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if ps[i] * 2 == total:
                    res += 2
                elif abs(total - 2*ps[i]) == 1:
                    res+= 1
        return res