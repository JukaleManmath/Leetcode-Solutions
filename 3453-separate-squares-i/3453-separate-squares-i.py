class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalarea , miny, maxy = 0.0 , float("inf"), float("-inf")
        for x , y , l in squares:
            totalarea += l * l
            miny = min(miny, y)
            maxy = max(maxy, y +l)
        
        for _ in range(80):
            mid = (miny + maxy) / 2
            areabelow = 0.0

            for x, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    areabelow += l * l
                else:
                    areabelow += l * (mid - y)
            if areabelow * 2 < totalarea:
                miny = mid
            else:
                maxy = mid
        
        return miny