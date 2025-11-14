class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n  = 0
        dummy = x
        while dummy:
            n = n * 10 +  dummy % 10
            dummy //= 10
        return n == x