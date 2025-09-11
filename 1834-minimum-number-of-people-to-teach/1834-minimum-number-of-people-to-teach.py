class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        need = set()

        for u , v in friendships:
            u -= 1
            v -= 1

            ok = False
            for i in languages[u]:
                if i in languages[v]:
                    ok = True
                    break
        
            if not ok:
                need.add(u)
                need.add(v)
        ans = float("inf")
        for i in range(1,n+1):
            curr = 0
            for j in need:
                if i not in languages[j]:
                    curr += 1
            ans = min(ans,curr)
        return ans
