class Solution:
    def ispalindrome(self, s, l , r):
        while l < r:
            if s[l] != s[r]:
                return False
            l , r = l + 1, r -1
        return True 
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.ispalindrome(s, i , j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return res
