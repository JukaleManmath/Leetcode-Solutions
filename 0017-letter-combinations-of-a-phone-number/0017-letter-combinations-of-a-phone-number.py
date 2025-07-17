class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mp = {
            "2": "abc",
            "3": "def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            for d in range(len(mp[digits[i]])):
                curr += mp[digits[i]][d]
                dfs(i+1, curr)
                curr = curr[:-1]
        if digits:
            dfs(0,"")
        return res
