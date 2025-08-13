class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # words = set(wordDict)
        # memo = {len(s) : True}
        # n = len(s)
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        
        #     for j in range(i + 1, n+1):
        #         if s[i:j] in words and dfs(j):
        #             memo[i] = True
        #             return True
        #     memo[i] = False
        #     return False
        # return dfs(0)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if(i + len(w) <= len(s) and s[i : i +len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]