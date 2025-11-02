class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        res = [[0 for _ in range(n)] for _ in range(m)]

        for g in guards:
            res[g[0]][g[1]] = 2
        for w in walls:
            res[w[0]][w[1]] = 3
        
        for i in range(m):
            for j in range(n):

                if res[i][j] == 2:
                    for row in range(i +1, m):
                        if res[row][j] in (2 ,3):
                            break
                        res[row][j] = 1
                    for row in range(i-1, -1, -1):
                        if res[row][j]in (2 ,3):
                            break
                        res[row][j] = 1
                    for col in range(j + 1, n):
                        if res[i][col] in (2 ,3):
                            break
                        res[i][col] = 1
                    
                    for col in range(j-1, -1, -1):
                        if res[i][col] in (2 ,3):
                            break
                        res[i][col] = 1
        cnt = 0
        for i in range(m):
            for j in range(n):
                if res[i][j] == 0:
                    cnt += 1
        return cnt
