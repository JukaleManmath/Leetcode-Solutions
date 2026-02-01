class Solution:
    def countMonobit(self, n: int) -> int:
        cnt =1
        while True:
            if 2 ** cnt - 1<= n:
                cnt += 1
            else:
                break

        return cnt