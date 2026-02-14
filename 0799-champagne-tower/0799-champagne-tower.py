class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass = [[0] * k for k in range(1, 102)]
        glass[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (glass[r][c] - 1.0) / 2.0
                if q > 0:
                    glass[r+1][c] += q
                    glass[r + 1][c + 1] +=q
        return min(1 , glass[query_row][query_glass])
        
