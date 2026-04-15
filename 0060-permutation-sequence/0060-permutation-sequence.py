class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        arr = []
        for i in range(1, n + 1):
            arr.append(i)
            fact *= i
        
        def rec(arr, fact, res,  k):
            if len(arr) == 1:
                res += str(arr[0])
                return res
            
            group = fact // len(arr)
            fact = fact // len(arr)
            currGroup = (k - 1) // group
            k = k - (currGroup * group)
            res += str(arr[currGroup])
            arr.pop(currGroup)
            return rec(arr, fact, res, k)
        return rec(arr, fact,"", k)