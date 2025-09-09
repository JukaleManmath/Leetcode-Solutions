class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        aware, spread, total = [0]* n,  0 , 1
        aware[0] = 1
        for i in range(1,n):
            if i>= delay:
                spread += aware[i-delay]
            if i >= forget:
                spread -= aware[i - forget]
                total -= aware[i- forget]
            total += spread
            aware[i] = spread
        
        return total % (10 **9 + 7)