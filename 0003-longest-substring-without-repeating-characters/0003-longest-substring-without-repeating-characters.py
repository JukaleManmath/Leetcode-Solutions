class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force
        longest = 0
        n = len(s)
        for i in range(n):
            arr = []
            for j in range(i, n):
                if s[j] not in arr:
                    arr.append(s[j])
                else:
                    break
            longest = max(longest, len(arr))
        return longest