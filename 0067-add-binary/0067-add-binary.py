class Solution:
    def addBinary(self, a: str, b: str) -> str:
        al , bl = -len(a), -len(b)
        carry , i = 0, -1
        res = ""
        while i >= al or i>= bl:
            abit = int(a[i]) if i >= al else 0
            bbit = int(b[i]) if i >= bl else 0

            s = abit+ bbit + carry
            res = str(s % 2) + res
            carry = s // 2
            i-= 1

        return "1" + res if carry else res
