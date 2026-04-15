class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum = str(num)

        res = 0
        for i in range(0, len(snum) - k + 1):
            curr = int(snum[i:i + k])
            if curr and num % curr == 0:
                res += 1
        return res