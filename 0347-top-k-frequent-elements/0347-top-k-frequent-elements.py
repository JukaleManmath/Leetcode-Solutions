class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force
        n = len(nums)
        frequent = {}
        for i in range(n):
            frequent[nums[i]] = 1 + frequent.get(nums[i], 0)
        sorted_items = sorted(frequent.items(), key=lambda x:x[1], reverse = True)
        return [item[0] for item in sorted_items[:k]]