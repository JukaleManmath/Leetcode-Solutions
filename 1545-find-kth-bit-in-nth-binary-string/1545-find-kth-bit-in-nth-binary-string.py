class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            res = ""
            for i in s:
                if i == "0":
                    res += "1"
                else:
                    res += "0"
            return res
        
        s = "0"
        for i in range(2, n + 1):
            reverse = invert(s)[::-1]
            s = s + "1" + reverse
        
        return s[k -1]