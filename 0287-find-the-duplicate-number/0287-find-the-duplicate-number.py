class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # map
        # map = {}
        # for i in nums:
        #     map[i] = 1 + map.get(i,0)
        #     if map.get(i,0) > 1:
        #         return i
        # return -1

        #set
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1