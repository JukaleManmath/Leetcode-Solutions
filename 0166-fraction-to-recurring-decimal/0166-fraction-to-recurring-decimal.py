class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        sign = "-" if numerator * denominator < 0 else ""
        n = abs(numerator)
        d = abs(denominator)
        integer = n // d
        r = n % d
        digit = []
        s = {}

        while r and r not in s:
            s[r] = len(digit)
            r = r * 10
            digit.append(str(r // d))
            r = r % d
        
        if r:
            i = s[r]
            dec = "".join(digit[:i]) + "(" + "".join(digit[i:]) + ")"
        else:
            dec = "".join(digit)
        
        return sign + str(integer) + "." + dec
         