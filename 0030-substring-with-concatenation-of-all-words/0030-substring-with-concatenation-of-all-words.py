class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        total = len(words) * l

        def freqmap(wordlist):
            freq = {}
            for ch in wordlist:
                freq[ch] = freq.get(ch, 0) + 1
            return freq
        
        main = freqmap(words)
        res = []
        for start in range(len(s) - total + 1):
            wordlist = [s[i:i+l] for i in range(start, start + total, l)]
            if freqmap(wordlist) == main:
                res.append(start)
        return res