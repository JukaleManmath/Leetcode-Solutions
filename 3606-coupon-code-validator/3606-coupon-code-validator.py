class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def isvalid(code):
            return code != "" and re.fullmatch(r"[A-Za-z0-9_]+", code) is not None
        categories = {
            "electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3
        }
        n = len(code)
        res = []
        for i in range(n):
            c , b , s = True, True, True
            if code[i] == "" or not isvalid(code[i]):
                c =  False
            if businessLine[i] not in categories:
                b = False
            if not isActive[i]:
                s = False
            if c and b and s:
                res.append([code[i], categories[businessLine[i]]])
        
        res.sort(key = lambda x: (x[1], x[0]))

        return [c[0] for c in res]