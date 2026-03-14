class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()
        print(res)
        n = len(res)
        l , r = 0, n - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True