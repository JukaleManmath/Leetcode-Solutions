class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            res = 0
            while n:
                rem = n % 10
                n = n // 10
                res += rem * rem
            return res

        slow, fast = n , next(n)

        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return True if fast == 1 else False
        