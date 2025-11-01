class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        l = nums2[-1]
        last = 10000000
        for a , b in zip(nums1, nums2):
            res += abs(a - b)

            if a <= l <= b or b <= l <= a:
                last = 0
            last = min(last , abs(a - l) , abs(b - l))
        return res + last + 1
