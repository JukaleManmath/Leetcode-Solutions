class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        # if target not in words:
        #     return -1
        # res1 = 0
        # i = startIndex
        # while words[i] != target:
        #     res1 += 1
        #     i  = ( i + 1) % n
        
        # res2 = 0
        # i = startIndex
        # while words[i] != target:
        #     res2 += 1
        #     i = (i - 1 + n) % n
        # return min(res1, res2)

        ans = n
        for i , word in enumerate(words):
            if word == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex))
        return ans if ans < n else -1