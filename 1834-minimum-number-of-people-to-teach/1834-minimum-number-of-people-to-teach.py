class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # so first we check all the freindships that can they communicate by checking ig their languages overlap
        # if not we add it to the set of needing a common language
        # after that we through all the language 1, n and with the help of greedy find the 
        # language which need min people to be taught so that everyone shares a common tongue
        
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
