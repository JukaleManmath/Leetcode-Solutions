class Solution:
    def myAtoi(self, s: str) -> int:
        int_min = -2 **31
        int_max = 2 ** 31 - 1
        n = len(s)
        neg = False
        num = "1234567890"
        res = ""
        i = 0
        while i < n:
            if s[i] == " ":
                i += 1
            else:
                break
        if i == n:
            return 0
        
        if s[i] == "-":
            neg = True
            i += 1
        elif s[i] == "+":
            neg = False
            i += 1

        while i < n:
            if s[i] == "0":
                i += 1
            else:
                break
        
        while i < n:
            if s[i] not in num:
                break
            res += s[i]
            i += 1
        
        ans = int(res) if len(res) > 0 else 0
        print(ans)
        if neg:
            ans = -1 * ans
        if ans < int_min:
            return int_min
        elif ans > int_max:
            return int_max
        else:
            return ans

