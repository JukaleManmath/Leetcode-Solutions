class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {len(s) : True}
        n = len(s)
        def dfs(i):
            if i in memo:
                return memo[i]
        
            for j in range(i + 1, n+1):
                if s[i:j] in words and dfs(j):
                    memo[j -i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)