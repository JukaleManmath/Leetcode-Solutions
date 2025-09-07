class Solution:
    def sumZero(self, n: int) -> List[int]:
        flag = True
        if n % 2 != 0:
            flag = False
        res = []
        counter = 0
        if flag:
            while len(res) < n:
                counter += 1
                res.append(-counter)
                res.append(counter)
                
            
        else:
            res.append(counter)
            while len(res)< n:
                counter += 1
                res.append(-counter)
                res.append(counter)
        return res


