class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        n = len(happiness) - 1
        ans = 0
        cnt = 0
        while cnt != k:
            if happiness[n] - cnt >= 0:
                ans += happiness[n] - cnt
            n -= 1
            cnt += 1
        return ans