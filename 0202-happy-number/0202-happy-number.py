class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            res = 0
            while n:
                rem = n % 10
                n = n // 10
                res += rem * rem
            return res

        slow = next(n)
        fast = next(next(n))
        if slow == 1 or fast == 1:
            return True
            
        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            else:
                slow = next(slow)
                fast = next(next(fast))
        return False
        