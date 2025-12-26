class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        opensum = [0] * n
        closesum = [0] * n

        for i in range(n):
            if customers[i] == "Y":
                opensum[i] += (opensum[i - 1] + 0) if i - 1>=0 else 0
                closesum[i] += (closesum[i-1] + 1) if i - 1 >= 0 else 1
            
            elif customers[i] == "N":
                opensum[i] += (opensum[i - 1] + 1) if i - 1>=0 else 1
                closesum[i] += (closesum[i-1] + 0) if i - 1 >= 0 else 0
        
        earliest = 0
        minpenalty = float("inf")

        for i in range(n + 1):
            currmin = closesum[n-1] - (closesum[i-1] if i -1 >= 0 else 0) + (opensum[i-1] if i-1 >= 0 else 0)
            if currmin < minpenalty:
                minpenalty = currmin
                earliest = i
        return earliest