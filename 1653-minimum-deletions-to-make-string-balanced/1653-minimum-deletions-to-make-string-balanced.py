class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        cnt = 0

        for c in s:
            if stack and stack[-1] == "b" and c == "a":
                stack.pop()
                cnt += 1
            else:
                stack.append(c)
        return cnt