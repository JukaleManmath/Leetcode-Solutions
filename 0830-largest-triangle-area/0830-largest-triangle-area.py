class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        n = len(points)
        points.sort()
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j + 1, n):
                    x1 , y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    a = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    area = max(area, a)
        return (1/2) * area