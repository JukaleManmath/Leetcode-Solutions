class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        res = ""
        nums = set(nums)
        n = len(nums)
        def backtrack(i, res):
            if i == n:
                if res not in nums:
                    return res[:]
                else:
                    return ""
            res += "0"
            ans = backtrack(i + 1, res)
            if ans:
                return ans
            res = res[:-1]
            res += "1"
            return backtrack(i + 1, res)
            
        return backtrack(0, "")
            