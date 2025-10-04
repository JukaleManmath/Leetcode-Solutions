class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = 0
        rem = 0

        while numBottles:
            total += numBottles

            emptybottles = numBottles + rem
            numFullBottles = 0
            while emptybottles >= numExchange:
                numFullBottles += 1
                emptybottles -= numExchange
                numExchange += 1
            numBottles = numFullBottles
            rem = emptybottles
        
        return total