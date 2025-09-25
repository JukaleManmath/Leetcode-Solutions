class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False
        
        seen = []
        for i in range(len(pattern)):
            if pattern[i] not in mp:
                if words[i] in seen:
                    return False
                mp[pattern[i]] = words[i]
                seen.append(words[i])
            else:
                if mp[pattern[i]] != words[i]:
                    return False
        return True

