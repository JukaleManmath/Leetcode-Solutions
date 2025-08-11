class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * (len(s) + 1)
        def dfs(i):
            if i == len(s):
                return 1
            if memo[i] != -1:
                return memo[i]
            if s[i] == '0':
                return 0

            memo[i] = dfs(i+1)
            if i + 1 <= len(s) -1:
                if(s[i] == "1" or (s[i]=="2" and s[i +1] <"7")):
                    memo[i] += dfs(i+2)
            return memo[i]
        return dfs(0)