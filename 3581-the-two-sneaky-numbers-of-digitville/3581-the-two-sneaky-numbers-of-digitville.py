class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        m = defaultdict(int)

        for i in nums:
            if m[i]:
                res.append(i)
            m[i] += 1
            if len(res) == 2:
                break
        return res
            
        