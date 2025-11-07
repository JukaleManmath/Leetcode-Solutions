class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        left , right = 0 , 10**12
        res = min(stations)
        n = len(stations)

        def ispossible(minpower, s, k):
            nonlocal n
            curr = 0
            le ,ri = 0 , r
            for i in range(r+ 1):
                curr += s[i]
            
            for i in range(n):
                if i - le > r:
                    curr -= s[le]
                    le += 1
                if ri - i < r and ri< n-1:
                    ri += 1
                    curr += s[ri]
                
                if curr < minpower:
                    power_needed = minpower - curr
                    if k < power_needed: return False
                    s[ri] += power_needed
                    curr += power_needed
                    k -= power_needed    
            return True
        
        while left <= right:
            mid = (left + right) // 2
            if ispossible(mid, stations[:], k):
                left = mid + 1
                res = mid     
            else:
                right = mid - 1
        return res

