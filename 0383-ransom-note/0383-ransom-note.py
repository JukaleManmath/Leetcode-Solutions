class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r , m = Counter(ransomNote), Counter(magazine)
        for ch in ransomNote:
            if ch not in magazine or r[ch] > m[ch]:
                return False
        return True