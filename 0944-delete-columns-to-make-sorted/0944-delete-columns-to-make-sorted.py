class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n = len(strs)
        sl = len(strs[0])
        arr = [""] * sl
          
        for i in range(n):
            for j in range(sl):
                arr[j] = arr[j] + strs[i][j]
        print(arr)
        for s in arr:
            print(sorted(s))
            if s != "".join(sorted(s)):
                cnt += 1
        return cnt