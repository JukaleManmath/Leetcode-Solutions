class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        n = len(s)
        res = []
        bal = 0
        i = 0
        for j in range(n):
            if s[j] == "1":
                bal += 1
            else:
                bal -= 1
            if bal == 0:
                new = self.makeLargestSpecial(s[i+1:j])
                res.append("1" + new + "0")
                i = j + 1
        res.sort(reverse=True)
        return "".join(res)