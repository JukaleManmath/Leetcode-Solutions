class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force
        # longest = 0
        # n = len(s)
        # for i in range(n):
        #     arr = []
        #     for j in range(i, n):
        #         if s[j] not in arr:
        #             arr.append(s[j])
        #         else:
        #             break
        #     longest = max(longest, len(arr))
        # return longest
        map = {}
        n = len(s)
        left, right = 0 , 0
        longest = 0
        while right < n:
            map[s[right]] = 1 + map.get(s[right], 0)
            if map[s[right]] > 1:
                while map[s[right]] > 1:
                    map[s[left]] -= 1
                    left += 1  
            longest = max(longest, right - left + 1)
            right += 1
        return longest