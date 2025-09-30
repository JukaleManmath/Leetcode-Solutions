class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")" : "(",
            "]": "[",
            "}":"{"
        }
        stack = []
        for i in range(len(s)):
            if s[i] in mp:
                if stack and mp[s[i]] == stack[-1]:
                     stack.pop()
                else:
                    return False 
            else:    
                stack.append(s[i])
        return len(stack) == 0
