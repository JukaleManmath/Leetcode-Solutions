class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        n = len(colors)
        time = 0
        ps = neededTime[0]
        maxval = neededTime[0]

        for i in range(1 , n):
            if colors[i] == colors[i-1]:
                ps += neededTime[i]
                maxval = max(maxval, neededTime[i])
            else:
                time += ps - maxval
                ps = neededTime[i]
                maxval = neededTime[i]
        return time + ps - maxval