class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # flag = True
        # res = -1
        # j = 0
        # while j < n:
        #     total = 0
        #     for i in range(0, n):
        #         k = (i+j)% n
        #         total += gas[k] - cost[k]
        #         if total < 0:
        #             flag = False
        #             break
        #     if flag:
        #         res = j
        #         break
        #     else:
        #         flag = True
        #         j += 1
        # return res

        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        res = 0
        total = 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i +1
                
        return res 


