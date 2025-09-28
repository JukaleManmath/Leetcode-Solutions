class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        res = [points[0]]
        for i in range(1, len(points)):
            if points[i][0] > res[-1][1]:
                res.append(points[i])
            else:
                x, y = res.pop()
                newInterval = [min(x, points[i][0]), min(y, points[i][1])]
                res.append(newInterval)
        return len(res)