class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = False
        n = len(s)
        if n == 1:
            return True
        i = 0
        while i < n:
            if s[i] == "1":
                if not flag:
                    while i < n and s[i] == "1":
                        i+= 1
                    flag = True
                else:
                    return False
            i += 1
        return flag
            