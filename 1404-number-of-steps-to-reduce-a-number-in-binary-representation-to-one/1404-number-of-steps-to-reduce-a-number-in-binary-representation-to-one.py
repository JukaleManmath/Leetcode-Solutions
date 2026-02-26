class Solution:
    def numSteps(self, s: str) -> int:
        # curr = int(s, 2)
        # res = 0
        
        # while curr != 1:
        #     if (curr & 1) == 0:
        #         curr = curr // 2
        #     else:
        #         curr += 1
                
        #     res += 1
        # return res

        res = 0
        carry = 0

        n = len(s)

        for i in range(n -1, 0 , -1):
            if int(s[i]) + carry == 1:
                carry = 1
                res += 2
            else:
                res += 1
        return res + carry
