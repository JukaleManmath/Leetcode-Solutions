class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        lr = defaultdict(list)
        tb = defaultdict(list)
        cnt = 0
        leftRight = set()

        for x, y in buildings:
            lr[x].append(y)
            tb[y].append(x)
        for i in lr:
            arr = sorted(lr[i])
            if len(arr) >= 3:
                for j in range(1, len(arr) - 1):
                    leftRight.add((i, arr[j]))
        for i in tb:
            arr = sorted(tb[i])
            if len(arr) >= 3:
                for j in range(1, len(arr) -1):
                    if (arr[j], i) in leftRight:
                        cnt += 1
        return cnt

