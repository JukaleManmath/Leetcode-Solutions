class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force - O(nlogn)
        # nums.sort()
        # for i in range(len(nums) -1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        # return -1

        # # map - O(n) and space - O(n)
        # map = {}
        # for i in nums:
        #     map[i] = 1 + map.get(i,0)
        #     if map.get(i,0) > 1:
        #         return i
        # return -1

        #set - O(n) and space - O(n)
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)
        # return -1

        # floyd's slow and fast pointer approach - O(n) and O(1) space
        slow , fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow