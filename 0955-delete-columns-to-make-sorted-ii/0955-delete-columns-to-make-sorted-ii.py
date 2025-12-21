class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n = len(strs[0])
        

        if len(strs) == 1:
            return 0
        
        sorted_pairs = [False] * (len(strs) - 1)

        for j in range(n):
            bad = False
            for i in range(len(strs) -1):
                if not sorted_pairs[i] and strs[i][j] > strs[i+ 1][j]:
                    bad = True
                    break
            if bad:
                cnt += 1
                continue
            for i in range(len(strs)-1):
                if not sorted_pairs[i] and strs[i][j] < strs[i+1][j]:
                    sorted_pairs[i] = True
        
        return cnt