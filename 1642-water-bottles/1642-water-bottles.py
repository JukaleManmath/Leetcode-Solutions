class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        rem = 0
        while numBottles:
            total += numBottles
            numEmpty = numBottles + rem
            numBottles = numEmpty // numExchange
            rem = numEmpty % numExchange
        return total
