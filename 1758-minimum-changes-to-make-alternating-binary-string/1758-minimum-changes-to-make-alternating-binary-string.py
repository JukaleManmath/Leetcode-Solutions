class Solution:
    def minOperations(self, s: str) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            if not stack or s[stack[-1]] != s[i]:
                stack.append(i)
            else:
                stack.pop()
                res += 1
        return res
