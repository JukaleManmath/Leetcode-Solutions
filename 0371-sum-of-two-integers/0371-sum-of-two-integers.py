class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            x = (a >> i) & 1
            y = (b >> i) & 1
            curr = x ^ y ^ carry
            carry = (x + y + carry) >= 2
            if curr:
                res |= (1 << i)
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res

