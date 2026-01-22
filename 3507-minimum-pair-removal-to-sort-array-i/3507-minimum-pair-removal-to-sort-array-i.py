class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        new = nums
        cnt = 0
        while True:
            if new == sorted(new):
                break
            minsum = float("inf")
            ind = -1
            n = len(new)
            for i in range(1, n):
                if new[i-1] + new[i] < minsum:
                    ind = i -1
                    minsum = new[i-1] + new[i]
            curr = []
            for i in range(n):
                if i == ind:
                    curr.append(minsum)
                elif i == ind + 1:
                    continue
                else:
                    curr.append(new[i])
            new = curr
            cnt += 1
        return cnt