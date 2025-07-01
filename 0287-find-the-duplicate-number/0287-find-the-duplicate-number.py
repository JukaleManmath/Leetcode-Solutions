class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            map[i] = 1 + map.get(i,0)
            if map.get(i,0) > 1:
                return i
        return -1