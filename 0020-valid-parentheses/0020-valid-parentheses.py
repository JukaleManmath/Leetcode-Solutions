class Solution:
    def matches(self, ch1, ch2):
        matche = {
            ')':'(',
            "}":"{",
            "]":"[",
        }
        return matche[ch1] == ch2

    def isValid(self, s: str) -> bool:
        st = deque()
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                st.append(ch)
            if ch == ")" or ch == "}" or ch == "]":
                if len(st) == 0:
                    return False
                if not self.matches(ch, st.pop()):
                    return False
        return len(st) == 0