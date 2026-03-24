class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: (x[1], x[0]), reverse = True)
        res = 0
        req = truckSize
        for i in range(len(boxTypes)):
            if boxTypes[i][0] > req:
                res += req * boxTypes[i][1]
                break
            else:
                res += boxTypes[i][0] *boxTypes[i][1]
                req -= boxTypes[i][0]
        return res