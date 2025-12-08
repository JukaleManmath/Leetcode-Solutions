class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for i in range(1 , n + 1):
            for j in range( i + 1, n+ 1):
                s = math.sqrt(i ** 2 + j ** 2)
                if int(s) == s and  s <= n:
                    cnt += 2
        return cnt