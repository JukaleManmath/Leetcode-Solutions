class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = [[] for _ in range(numRows)]
        turn = 1
        j = 0
        n = len(s)

        for i in range(n):
            res[j].append(s[i])
            j += turn
            if j == numRows:
                j = numRows - 2
                turn = -1
            if j == -1:
                j = 1
                turn = 1

        ans = ""
        for arr in res:
            ans += "".join(arr)
        return ans

            
                