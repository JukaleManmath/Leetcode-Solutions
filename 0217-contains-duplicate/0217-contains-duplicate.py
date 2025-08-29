class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # cnt = {}
        # for i in nums:
        #     cnt[i] = cnt.get(i, 0) + 1
        # for k in cnt:
        #     if cnt[k] >= 2:
        #         return True
        # return False

        res = set()
        for i in nums:
            if i in res:
                return True
            res.add(i)
        return False
 