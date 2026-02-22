class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)
        st = []
        res = 0
        for bit in range(len(s)):
            if s[bit] == "1":
                if st:
                    last = st.pop()
                    res = max(res, bit -last)
                st.append(bit)
                print(st)

        return res
