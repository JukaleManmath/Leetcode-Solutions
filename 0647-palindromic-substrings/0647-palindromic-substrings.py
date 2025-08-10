class Solution:
    def countSubstrings(self, s: str) -> int:
        # cnt = 0 
        # for i in range(len(s)):
        #     l = i
        #     r = i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         cnt += 1
        #         l -= 1
        #         r += 1
            
        #     l , r = i , i + 1
        #     while l >=0 and r < len(s) and s[l] == s[r]:
        #         cnt +=1
        #         l-=1
        #         r +=1
        # return cnt

        cnt = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    cnt += 1
        return cnt