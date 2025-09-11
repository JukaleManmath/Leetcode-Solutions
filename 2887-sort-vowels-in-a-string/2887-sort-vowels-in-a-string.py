class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        char = []
        t = ""
        for ch in s:
            if ch in vowels:
                char.append(ch)
        char.sort()

        i = 0
        for ch in s:
            if ch in vowels:
                t += char[i]
                i += 1
            else:
                t += ch
        return t
