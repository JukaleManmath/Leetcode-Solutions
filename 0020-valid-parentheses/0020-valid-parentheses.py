class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        for i in s:
            if i in mp:
                if stack and stack[-1] == mp[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0