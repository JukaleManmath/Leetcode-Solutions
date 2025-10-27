class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n , m = len(bank), len(bank[0])
        lasers = []
        cnt = 0

        for i in range(n):
            c = 0
            for j in range(m):
                if bank[i][j] == "1":
                    c += 1
            if c:
                lasers.append(c) 
        
        print(lasers)
        for i in range(1, len(lasers)):
            cnt += lasers[i] * lasers[i-1]
        return cnt