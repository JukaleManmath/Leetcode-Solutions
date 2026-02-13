class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        # 1st case if longest substr only have single unique char
        i = 0
        while i < n:
            j  = i
            while j < n and s[i] == s[j]:
                j += 1
            ans = max(ans, j - i)
            i = j
        print(ans)
        # case 2 we consider 2 chars and ignore 1 if they form the longest
        def helper(a, b, c):
            best = 0
            diff = 0
            mp = {}
            cnt = 0
            mp[(0,0)] = -1
            for i in range(n):
                if s[i] == c:
                    cnt += 1
                    mp[(diff, cnt)] = i
                    continue
                if s[i] == a:
                    diff += 1
                elif s[i] == b:
                    diff -= 1
                if (diff, cnt ) in mp:
                    best = max(best, i - mp[(diff, cnt)])
                else:
                    mp[(diff, cnt)] = i
            return best
        
        ans = max(ans, helper("a", "b","c"))
        print(ans)
        ans = max(ans, helper("b", "c","a"))
        print(ans)
        ans = max(ans, helper("a", "c","b"))

        #case 3 where abc form the longest balanced substr
        print(ans)
        cnt_a , cnt_b ,cnt_c = 0 , 0 ,0
        mp = defaultdict(int)
        mp[(0,0)] = -1
        for i in range(n):
            if s[i] == "a":
                cnt_a += 1
            elif s[i] == "b":
                cnt_b += 1
            else: 
                cnt_c += 1
            
            d1 = cnt_a - cnt_b
            d2 = cnt_a - cnt_c
            if (d1, d2) in mp:
                ans = max(ans , i  - mp[(d1,d2)])
            else:
                mp[(d1, d2)] = i
        print(ans)
        return ans




