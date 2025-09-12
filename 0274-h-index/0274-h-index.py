class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_h = 0
        n = len(citations)
        for i in range(1, n+1):
            cnt = 0
            for j in range(n):
                if citations[j] >= i:
                    cnt += 1
                if cnt == i:
                    max_h = max(max_h, cnt)
                    break
        return max_h