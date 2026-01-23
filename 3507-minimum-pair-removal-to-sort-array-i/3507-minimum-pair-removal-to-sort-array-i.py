class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # new = nums
        # cnt = 0
        # while True:
        #     if new == sorted(new):
        #         break
        #     minsum = float("inf")
        #     ind = -1
        #     n = len(new)
        #     for i in range(1, n):
        #         if new[i-1] + new[i] < minsum:
        #             ind = i -1
        #             minsum = new[i-1] + new[i]
        #     curr = []
        #     for i in range(n):
        #         if i == ind:
        #             curr.append(minsum)
        #         elif i == ind + 1:
        #             continue
        #         else:
        #             curr.append(new[i])
        #     new = curr
        #     cnt += 1
        # return cnt

        cnt = 0
        while len(nums) > 1:
            isAscending = True
            minsum = float("inf")
            targetIndex = -1

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if nums[i] > nums[i + 1]:
                    isAscending = False
                
                if pair_sum < minsum:
                    minsum = pair_sum
                    targetIndex = i
            
            if isAscending:
                break
            cnt += 1
            nums[targetIndex] = minsum
            nums.pop(targetIndex + 1)
        
        return cnt