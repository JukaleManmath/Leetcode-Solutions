class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        # dp = {}
        # def dfs(i , s):
        #     if i >= n:
        #         return 0
        #     if (i ,s) in dp:
        #         return dp[(i,s)]
        #     if s % 3 == 0:
        #         return s
            
        #     dp[(i, s)] = max(dfs(i +1, s), dfs(i + 1, s -nums[i]))
        #     return dp[(i, s)]
        
        # return dfs(0, total)

        smallest_one = float("inf")
        smallest_two = float("inf")

        for i in nums:
            total += i
            if i % 3 == 1:
                smallest_two = min(smallest_two, smallest_one +i)
                smallest_one = min(smallest_one, i)
            if i % 3 == 2:
                smallest_one = min(smallest_one, smallest_two + i)
                smallest_two = min(smallest_two, i)
        
        if total% 3 == 0:
            return total
        if total % 3 == 1:
            return total - smallest_one
        if total % 3 == 2:
            return total - smallest_two
        
                
        