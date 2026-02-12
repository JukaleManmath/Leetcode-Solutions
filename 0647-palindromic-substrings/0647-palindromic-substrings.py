class Solution:
    def countSubstrings(self, s: str) -> int:
        # cnt = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substr = s[i:j+1]
        #         if  substr == substr[::-1]:
        #             cnt += 1
        # return cnt

        cnt = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            
            l , r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
        return cnt