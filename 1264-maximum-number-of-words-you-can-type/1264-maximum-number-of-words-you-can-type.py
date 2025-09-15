class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split()
        res = 0
        for i in range(len(arr)):
            for ch in brokenLetters:
                if ch in arr[i]:
                    res += 1
                    break
        return len(arr) - res
