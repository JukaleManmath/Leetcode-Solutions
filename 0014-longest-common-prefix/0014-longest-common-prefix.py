class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort()
        # first , last = strs[0] , strs[-1]
        # res = ""
        # for i in range(min(len(first), len(last))):
        #     if first[i] != last[i]:
        #         return res
            
        #     res += first[i]
        
        # return res        

        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[:pref_len]
        return pref