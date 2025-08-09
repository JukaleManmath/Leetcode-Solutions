class Solution:
    def longestPalindrome(self, s: str) -> str:
        #  Two pointers approach O(n2) - time and space -O(1)
        # res = ""
        # resLen = 0
        # for i in range(len(s)):
        #     l, r = i, i
            
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if resLen < r - l + 1:
        #             res =  s[l:r + 1]
        #             resLen = r - l + 1
        #         r += 1
        #         l -= 1
            
        #     l , r = i, i + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if resLen < r - l + 1:
        #             res = s[l:r + 1]
        #             resLen = r-l + 1
        #         r += 1
        #         l -= 1
        # return res    

        # Recursive  + Memoization
        # memo = {}
        # res = ""
        # def dfs(l , r):
        #     nonlocal res
        #     if (l, r) in memo:
        #         return memo[(l, r)]
        #     substring = s[l : r + 1]
        #     if substring == substring[::-1]:
        #         if len(res) < len(substring):
        #             res = substring
        #         memo[(l,r)] = substring
        #         return substring
        #     dfs(l+1 ,  r)
        #     dfs(l , r - 1)
        #     memo[(l,r)] = ""
        #     return ""
        # dfs(0, len(s) - 1)
        # return res

        # DP

        idx , reslen = 0 , 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if reslen < j - i + 1:
                        idx = i
                        reslen = j - i + 1
        return s[idx: idx + reslen]